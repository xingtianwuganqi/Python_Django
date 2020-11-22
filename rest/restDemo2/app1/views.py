# import json

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import DegreeCourse,Course,PricePolicy

def test(request):
    objc = DegreeCourse.objects.filter(title = 'Python全栈').first()
    PricePolicy.objects.create(price=9.9,period=30,content_type=objc)

    # 根据价格id获取课程，获取全部的价格策略
    course = Course.objets.filter(id=1).first()
    price_policys = course.price_policy_list.all()


    return HttpResponse('...')