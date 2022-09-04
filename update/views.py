from django.http import HttpResponse
from django.shortcuts import render,redirect
import docker
import os, subprocess

def update(request,servicename):
    client = docker.from_env() # docker api client 불러오기
    if request.method == "GET":
        return render(request, 'service/update.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        image_name = request.POST.get('image_name')

        service_name = servicename # 업데이트할 서비스 이름(웹에서 선택)
    
        service = client.services.get(service_name) # service 객체 받아오기
        service.update(image=image_name) # 업데이트

        return redirect('/service/list')

def rollback(request,servicename):

    service_name = servicename # 웹에서 받아올 rollback 할 서비스 이름
    command = 'docker service rollback ' + service_name # 롤백 명령어 작성

    ret = subprocess.run(command, shell=True, check=True) # 롤백 명령어 실행


    return redirect('/service/list')

def scale(request,servicename):
    client = docker.from_env()
    if request.method == "GET":
        return render(request, 'service/scale.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        count = request.POST.get('scale_num')

        service_name = servicename # 업데이트할 서비스 이름(웹에서 선택)

        service = client.services.get(service_name) # service 객체 받아오기
        scale_num =  int(count)
        service.scale(scale_num)
        return redirect('/service/list')

