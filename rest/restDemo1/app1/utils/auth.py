
from django.shortcuts import render
from django.http import JsonResponse
from app1 import models
from rest_framework.request import Request
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class Authtication(BaseAuthentication):

    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest_framework 内部会将两个字段赋值给request，以供后续使用 request.user request.auth
        return (token_obj.user,token_obj)

    def authenticate_header(self,request):
        pass
