import json

from django.shortcuts import render,HttpResponse

def users(request):
    user_list = ['alex','oldboy']
    return HttpResponse(json.dumps((user_list)))


from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        ret = super(studentsView,self).dispatch(request,*args,**kwargs)
        return ret

# 装饰器，
# @csrf_exempt
@method_decorator(csrf_exempt,name='dispatch')
class studentsView(MyBaseView,View):

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

    def get(self,request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self,request, *args, **kwargs):
        return HttpResponse('POST')


class TearchersView(MyBaseView, View):


    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')



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
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('alex',None)
    def authenticate_header(self,val):
        pass

class DogView(APIView):
    # 登录认证
    authentication_classes = [MyAuthentication]

    def get(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")
    def post(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")
    def put(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")
    def delete(self,request, *args, **kwargs):
        return HttpResponse("获取Dog")