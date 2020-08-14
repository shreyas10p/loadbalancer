import os
from django.http import JsonResponse
import time


def sample(request):
    time.sleep(1)
    return JsonResponse({'app':os.environ["APP"]})

def healthres(request):
    return JsonResponse({status:"ok"})

