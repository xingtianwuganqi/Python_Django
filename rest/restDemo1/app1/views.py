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