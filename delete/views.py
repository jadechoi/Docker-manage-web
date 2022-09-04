from django.shortcuts import render,redirect
from django.http import HttpResponse
import os, subprocess

def stack_remove(requests,stackname):
   # remove.sh 의 경로
    remove_path = os.getcwd() + '/deploy_data/shell/stack_remove.sh'
    stack_name = stackname # 받아올 stack의 이름
    command = remove_path + ' ' + stack_name # shell 파일 실행 명령어 작성

   # remove.sh 실행
    ret = subprocess.run(command, shell=True, check=True)
    return redirect('/stack/list')

def net_remove(requests,netname):
   # remove.sh 의 경로
    remove_path = os.getcwd() + '/deploy_data/shell/net_remove.sh'
    network_name = netname # 받아올 stack의 이름
    command = remove_path + ' ' + network_name # shell 파일 실행 명령어 작성

   # remove.sh 실행
    ret = subprocess.run(command, shell=True, check=True)
    return redirect('/network/list')

def vol_remove(requests, volname):
   # remove.sh 의 경로
    remove_path = os.getcwd() + '/deploy_data/shell/vol_remove.sh'
    vol_name = volname # 받아올 stack의 이름
    command = remove_path + ' ' + vol_name # shell 파일 실행 명령어 작성

   # remove.sh 실행
    ret = subprocess.run(command, shell=True, check=True)
    return redirect('/volume/list')
