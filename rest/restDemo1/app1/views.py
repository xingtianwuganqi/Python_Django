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
from rest_framework.request import Request
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import BaseAuthentication
from app1.utils.permission import MyPermission
from rest_framework.throttling import BaseThrottle
import time
from app1.utils.throttle import UserThrottle
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
VISIT_RECORD = {}


def md5(user):
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class VisitThrottle(object):
    '''
    60s内只能访问3次
    可以存到数据库，redis
    '''
    def __init__(self):
        self.history = None

    def allow_request(self,request,view):
        # 1.获取用户ip
        remote_addr = request.META.get('REMOTE_ADDR')
        print(remote_addr)
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime,]
            return True
        history = VISIT_RECORD.get(remote_addr)
        self.history = history
        while history and history[-1] < ctime - 60:
            history.pop()

        if len(history) < 3:
            history.insert(0,ctime)
            return True

        return False  # False 访问频率太高，被限制

    def wait(self):
        # 需要等待多少秒
        ctime = time.time()
        second = 60 - (ctime - self.history[-1])
        return second

class AnthView(APIView):

    '''
    登录
    '''
    authentication_classes = []
    permission_classes = []
    throttle_classes = [VisitThrottle]
    def post(self,request,*args,**kwargs):

        # 1.request中获取ip
        # 2.访问记录



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
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def post(self,request,*args,**kwargs):
        ret = {
            'code': 1000,
            'msg': None
        }
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

        return JsonResponse(ret)

ORDER_DICT = {
    1:{
        'name':'杏子',
        'age': 19,
        'gender':'女',
        'content': '呵呵'
    },
    2:{
        'name':'狗子',
        'age': 18,
        'gender':'男',
        'content': '哈哈'
    }
}

# class Authtication(object):
#
#     def authenticate(self,request):
#         token = request._request.GET.get('token')
#         token_obj = models.UserToken.objects.filter(token=token).first()
#         if not token:
#             raise exceptions.AuthenticationFailed('用户认证失败')
#         # 在rest_framework 内部会将两个字段赋值给request，以供后续使用 request.user request.auth
#         return (token_obj.user,token_obj)
#
#     def authenticate_header(self,request):
#         pass


class OrderView(APIView):
    '''
    订单相关业务
    '''

    # authentication_classes = []
    permission_classes = [MyPermission]
    throttle_classes = [UserThrottle] # 访问评论
    def get(self,request,*args, **kwargs):


        ret = {'code': 1000,'msg': None,'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)

class ParamVersion(object):
    def determine_version(self,request,*args,**kwargs):
        versions = request.query_params.get('version')
        return versions

from django.urls import reverse

class UsersView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    # 版本处理
    # versioning_class = ParamVersion
    # versioning_class = QueryParameterVersioning
    # versioning_class = URLPathVersioning
    def get(self,request,*args,**kwargs):
        # version = request._request.GET.get('version')
        # versions = request.query_params.get('version')
        # self.dispatch
        # 获取版本
        print(request.version)
        # 获取处理版本的对象
        print(request.versioning_scheme)
        # 反向生成url
        u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
        print(u1)
        # django反向生成url
        u2 = reverse(viewname='uuu',kwargs={'version': 1})
        print(u2)

        return HttpResponse('用户列表')

class DjangoView(APIView):
    def get(self,request, *args, **kwargs):
        print(type(request._request))
        return HttpResponse('POST和body')

from rest_framework.parsers import JSONParser,FormParser
class ParserView(APIView):
    '''
    JSONParser
    表示允许用户发送json数据
    a.content-type: application/json
    b.{name:alex,age:18}

    FormParser
    支持form表单请求
    content-type:application/x-www-form-urlencoded
    '''
    # parser_classes = [JSONParser,FormParser]
    def post(self,request, *args, **kwargs):
        # 获取解析后的结果
        '''
        1.获取用户的请求头
        2.获取用户的请求体
        3.根据用户请求头和parser_classes = [JSONParser,FormParser]中支持的请求头进行比较
        4.JSONParser对象去处理请求体
        5.request.data
        '''
        print(request.data)
        self.dispatch
        return HttpResponse('POST和body')

# 自定义字段
from rest_framework import serializers
# class RolesSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     usertype = serializers.IntegerField(source="user_type")
    # type = serializers.IntegerField(source='get_user_type_display') # 获取用户类型的形容词
    # gp = serializers.CharField(source='group.id') # 获取关联表的数据
    # gp_title = serializers.CharField(source='group.title')
    # # 获取角色的所有数据,自定义显示
    # rls = serializers.SerializerMethodField()
    #
    # def get_rls(self,row):
    #     role_objc_list = row.roles.all()
    #     ret = []
    #     for item in role_objc_list:
    #         ret.append({'id':item.id,'title':item.title})
    #     return ret

class RolesSerializer(serializers.ModelSerializer):
    usertype = serializers.IntegerField(source="user_type")
    # rls = serializers.SerializerMethodField()
    '''
    返回的group参数是url
    '''
    # group = serializers.HyperlinkedIdentityField(view_name='gp', lookup_field ='group_id', lookup_url_kwarg = 'pk')


    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ('id','username','user_type','usertype')
    # def get_rls(self,row):
    #     role_objc_list = row.roles.all()
    #     ret = []
    #     for item in role_objc_list:
    #         ret.append({'id':item.id,'title':item.title})
    #     return ret

class RolesView(APIView):

    # def get(self,request,*args,**kwargs):
    #     # 方式一
    #     roles = models.Role.objects.all().values('id','title')
    #     roles = list(roles)
    #     ret = json.dump(roles)
    #     return HttpResponse(ret)


    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        # user = models.UserInfo.objects.all().values('username','user_type')
        # user = list(user)
        # users = json.dumps(user,ensure_ascii=False)

        #方式二：对于[obj,obj,obj]
        rest_user = models.UserInfo.objects.all()
        print(rest_user)
        '''
        many=True对应数组 （many=False）单个数据
        生成链接需要context参数
        '''
        ser = RolesSerializer(instance=rest_user,many=True,context={'request': request})
        ser_data = json.dumps(ser.data,ensure_ascii=False)

        return HttpResponse(ser_data)

# 类校验方法
class TitleValidatar(object):
    def __init__(self,base):
        self.base = base

    def __call__(self, value):
        if not value.startwith(self.base):
            message = '标题已%s为开头' % self.base
            raise serializers.ValidationError(message)
    def set_context(self,serializer_field):
        # 执行验证之前调用，serializer_field是当前字段对象
        pass

class GroupSerializer(serializers.ModelSerializer):
    title = serializers.EmailField(error_messages={'required':'标题不能为空'},validators=[TitleValidatar('Django')])
    class Meta:
        model = models.UserGroup
        fields = "__all__"

    # 钩子方法校验
    def validate_title(self,value):
        from rest_framework import exceptions
        if not value:
            raise exceptions.ValidationError('不能为空')
        return value

class GroupView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,*args,**kwargs):
        # 从URL传参中获取pk参数
        pk = kwargs.get('pk')
        group = models.UserGroup.objects.filter(pk=pk).first()
        ser = GroupSerializer(instance=group,many=False)
        # 验证
        if ser.is_valid():
            print(ser.validated_data['title'])
        else:
            print(ser.errors)
        ser_data = json.dumps(ser.data)
        return HttpResponse(ser_data)


