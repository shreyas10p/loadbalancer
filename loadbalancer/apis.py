from django.http import JsonResponse
import requests
import json
import yaml
from .utils import *

SERVER_1 = "localhost:8081"
SERVER_2 = "localhost:8082"
SERVER_3 = "localhost:9081"

config = load_config('loadbalancer.yaml')
register = server_from_config(config)

# HOST based Routing
def host_routing(request):
    updated_reg = healthcheck(register)
    header = request.META.get('HTTP_HOST')
    for entry in config['hosts']:
        if(header == entry['host']):
            healthy_server = get_healthy_server(header,updated_reg)
            if(healthy_server):
                healthy_server._requestCount += 1
                res = requests.get('http://{}'.format(healthy_server._url))
                healthy_server._requestCount -= 1
                result = json.loads(res.content.decode('utf-8'))
                return JsonResponse({'status_code':200,'content':result})
            return JsonResponse({'status_code':503,'content':'No Server Available'})
    return JsonResponse({'status_code':404,'content':'Not Found'})


#PATH Based Routing
def server1_path(request):
    res = requests.get('http://{}'.format(SERVER_1))
    result = json.loads(res.content.decode('utf-8'))
    return JsonResponse({'status_code':res.status_code,'content':result})

def server2_path(request):
    res = requests.get('http://{}'.format(SERVER_2))
    result = json.loads(res.content.decode('utf-8'))
    return JsonResponse({'status_code':res.status_code,'content':result})

def server3_path(request):
    res = requests.get('http://{}'.format(SERVER_3))
    result = json.loads(res.content.decode('utf-8'))
    return JsonResponse({'status_code':res.status_code,'content':result})



