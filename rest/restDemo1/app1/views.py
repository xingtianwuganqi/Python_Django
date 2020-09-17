import json

from django.shortcuts import render,HttpResponse

def users(request):
    user_list = ['alex','oldboy']
    return HttpResponse(json.dumps((user_list)))