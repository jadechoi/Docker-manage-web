from django.shortcuts import render,redirect
from django.http import HttpResponse
from create.forms import CreateForm, CreateNetworkForm, CreateVolumeForm

# Create your views here.
import docker
import os, subprocess

def create(request):
    # form page 띄우기 
    if request.method == "GET":

        return render(request, 'stack/create.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        name = request.POST.get('stack_name')
        yml = request.POST.get('create_yml')
        deploy_data_path = os.getcwd() + '/deploy_data'
        
        with open('/home/rapa/project/docker_manage/deploy_data/yml/temp.yml', 'w') as f:

            f.write(yml)

        yml_path = deploy_data_path + '/yml/temp.yml' # yml 파일 경로
        stack_name = name # 받아올 stack/service name
        sh_path = deploy_data_path + '/shell/deploy.sh' # shell 파일 경로
        command = sh_path + ' ' + yml_path + ' ' + stack_name # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)
        return redirect('/stack/list')

def netcreate(request):
    if request.method == "GET":

        return render(request, 'network/create.html')

    # form으로 입력받은 데이터 저장 밑 네트워크 생성
    elif request.method == "POST":
        netname = request.POST.get('network_name')
        driver_o = request.POST.get('driver')
        attachable = request.POST.get('attachable')

        deploy_data_path = os.getcwd() + '/deploy_data'
        net_name = str(netname)
        driver = str(driver_o)

        if attachable == True:
            sh_path = deploy_data_path + '/shell/netcreate.sh' # shell 파일 경로
            command = sh_path + ' ' + driver + ' ' + '--attachable' + ' ' + net_name # 실행할 명령어
        else:
            sh_path = deploy_data_path + '/shell/netcreate_false.sh' # shell 파일 경로
            command = sh_path + ' ' + driver + ' ' + net_name

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)
        return redirect('/network/list')

def volcreate(request):
    if request.method == "GET":

        return render(request, 'volume/create.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        volname = request.POST.get('vol_name')

        deploy_data_path = os.getcwd() + '/deploy_data'
        vol_name = str(volname)

        sh_path = deploy_data_path + '/shell/volcreate.sh' # shell 파일 경로
        command = sh_path + ' ' + vol_name

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)
        return redirect('/volume/list')

def mainpage(request):
    return render(request, 'index.html')

def dockerhub_login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        ids = request.POST.get('docker_id')
        pws = request.POST.get('token')

        docker_id = str(ids) 
        docker_pw = str(pws)

        deploy_data_path = os.getcwd() + '/deploy_data'
        sh_path = deploy_data_path + '/shell/login.sh' # shell 파일 경로
        command = sh_path + ' ' + docker_id + ' ' + docker_pw # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)

        return redirect('/')

def logout_docker(request):
        deploy_data_path = os.getcwd() + '/docker_manage/deploy_data'

        sh_path = deploy_data_path + '/shell/logout.sh' # shell 파일 경로
        command = sh_path # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)

        return redirect('/')
