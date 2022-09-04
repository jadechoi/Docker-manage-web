from django.shortcuts import HttpResponse, render
import os

def stack_list(request): 
    stack_comm = 'docker stack ls'

   # 명령어 실행 stream
    stack_stream = os.popen(stack_comm)

   # 명령어 실행 결과 받아오기
    stack_stream_output = stack_stream.read()

   # 출력용 결과
    result = stack_stream_output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))

    return render(request, 'stack/tables.html', {'stacks':stacks, })

def service_list(request): 
    service_comm = 'docker service ls'

   # 명령어 실행 stream
    service_stream = os.popen(service_comm)

   # 명령어 실행 결과 받아오기
    service_stream_output = service_stream.read()

   # 출력용 결과
    result =  service_stream_output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))

    return render(request, 'service/tables.html', {'stacks':stacks, })

def stack_ps(request, stackname):
   # urls.py 에 'list/stack-ps' 로 했는데 각자 알아서 할것
    stack_name = stackname   # 웹에서 전달 받을 stack name
    command = 'docker stack ps ' + stack_name # 명령어 작성
    
    # 명령어 실행 및 결과
    stream = os.popen(command)
    output = stream.read()

    result = output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))

    return render(request, 'stack/tables_ps.html', {'stacks':stacks, })



def service_ps(request,servicename):
   # urls.py 에 'list/service-ps' 로 했는데 각자 알아서 할것
    service_name= servicename # 웹에서 전달 받을 service name
    command = 'docker service ps ' + service_name # 명령어 작성
    
    # 명령어 실행 및 결과
    stream = os.popen(command)
    output = stream.read()

    result = output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))
    return render(request, 'service/tables_ps.html', {'stacks':stacks, })

def network_list(request):
    net_comm = 'docker network ls'
    net_stream = os.popen(net_comm)
    net_stream_output = net_stream.read()
    result = net_stream_output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))

    return render(request, 'network/tables.html', {'stacks':stacks, })

def network_inspect(request,netname):
    net_name = netname
    net_ins_comm = 'docker network inspect ' + net_name
    net_stream = os.popen(net_ins_comm)
    net_stream_output = net_stream.read()
    result = "<pre>"
    result += net_stream_output
    result += "</pre>"

    return HttpResponse(result)

def volume_list(request):
    vol_comm = 'docker volume ls'
    vol_stream = os.popen(vol_comm)
    vol_stream_output = vol_stream.read()
    result = vol_stream_output
    stacks = []
    lines = result.split('\n')
    for line in lines:
        if 'NAME' in line : continue
        elif len(line) == 0 : continue
        else:
            stacks.append(list(line.split()))

    return render(request, 'volume/tables.html', {'stacks':stacks, })

def volume_inspect(request, volname):
    vol_name = volname
    vol_ins_comm = 'docker volume inspect ' + vol_name
    vol_stream = os.popen(vol_ins_comm)
    vol_stream_output = vol_stream.read()
    result = "<pre>"
    result += vol_stream_output
    result += "</pre>"
    return HttpResponse(result)

def profile_inspect(request):
    profile_ins_comm = 'cat /home/rapa/.docker/config.json'
    profile_stream = os.popen(profile_ins_comm)
    profile_stream_output = profile_stream.read()
    result = "<pre>"
    result += profile_stream_output
    result += "</pre>"
    return HttpResponse(result)
