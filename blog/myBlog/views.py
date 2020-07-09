from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('欢迎使用django！')

def index(request):
    # 添加两个变量，并给它们赋值
    sitename = 'Django 中文网'
    url = 'www.django.cn'
    # 新加一个列表
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    # 在来的基础上新加一个字典
    mydict = {
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }
    # 把两个变量封装到上下文里
    context = {
        'sitename': sitename,
        'url': url,
        'list':list,
        'mydict': mydict,
    }
    # 把上下文传递到模板里
    return render(request,'index.html',context)
