import json

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def users(request):
    user_list = ['alex','oldboy']
    return HttpResponse(json.dumps((user_list)))
#
#
#
#
#
# class MyBaseView(object):
#     def dispatch(self, request, *args, **kwargs):
#         ret = super(studentsView,self).dispatch(request,*args,**kwargs)
#         return ret

# 装饰器，
# @csrf_exempt
# @method_decorator(csrf_exempt,name='dispatch')
# class studentsView(MyBaseView,View):

# 通过dispatch映射，找到请求的方法，然后对应def的get，post
    # def dispatch(self, request, *args, **kwargs):
    #     func = getattr(request.method.lower())
    #     ret = func(request, *args, **kwargs)
    #     return ret

    # 重写父类dispatch方法
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     ret = super(studentsView,self).dispatch(request,*args,**kwargs)
    #     return ret

#     def get(self,request, *args, **kwargs):
#         return HttpResponse('GET')
#
#     def post(self,request, *args, **kwargs):
#         return HttpResponse('POST')
#
#
# class TearchersView(MyBaseView, View):
#
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('GET')
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse('POST')

# def get_order(request):
#     pass
#
#
# def del_order(request):
#     pass
#
#
# def update_order(request):
#     pass

from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET('token')
        # 获取用户名和密码，去数据库校验
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('alex',None)
    def authenticate_header(self,val):
        pass

class DogView(APIView):
    # 登录认证
    authentication_classes = [MyAuthentication]

    def get(self,request, *args, **kwargs):
        print(request)
        print(request.user)
        return HttpResponse("获取Dog")
    def post(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")
    def put(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")
    def delete(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")

from django.shortcuts import render
from django.http import JsonResponse
from app1 import models

def md5(user):
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class AnthView(APIView):

    def post(self,request,*args,**kwargs):
        ret = {'code':1000,'msg':None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            token = md5(user)
            # 存在就更新，不存在就创建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)


class UserView(APIView):

    def post(self,request,*args,**kwargs):
        ret = {
            'code': 1000,
            'msg': None
        }
        print(request._request)
        try:
            username = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            print(username,pwd)
            check = models.UserInfo.objects.filter(username=username).first()
            if check:
                ret['code'] = 1004
                ret['msg'] = '该号码已注册'
                return JsonResponse(ret)

            if username == None or pwd == None:
                ret['code'] = 1003
                ret['msg'] = '请输入用户名或密码'
                return JsonResponse(ret)

            obj = models.UserInfo.objects.create(username=username,password=pwd,user_type=1)
            token = md5(username)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = '请求异常'
            print(ret)

        return JsonResponse(ret)






