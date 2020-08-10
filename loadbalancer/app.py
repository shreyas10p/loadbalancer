import os
from django.http import JsonResponse

def sample(request):
    return JsonResponse({'app':os.environ["APP"]})

def healthcheck(request):
    return JsonResponse({status:"ok"})
