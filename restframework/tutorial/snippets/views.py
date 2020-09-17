from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from .models import Snippet
# from .serializers import SnippetSerializer
#
# class JSONResponse(HttpResponse):
#
#     def __init__(self,data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)
#
# @csrf_exempt # 请注意，因为我们希望能够从不具有CSRF令牌的客户端对此视图进行post，因此我们需要将视图标记为csrf_exempt
# def snippet_list(request):
#     '''
#     列出所有的code snippet,或创建一个新的snippet
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=201)
#         return JSONResponse(serializer.errors,status=400)
#
#
# @csrf_exempt
# def snippet_detail(request,pk):
#     '''
#     获取、更新、或删除一个 code snippet
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=400)
#
#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors,status=400)
#
#     elif request.method == "DELETE":
#         snippet.delete()
#         return HttpResponse(status=400)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer

'''
REST 框架引入乐乐一个扩展了常规HttpRequest的Request对象，并提供了更灵活的请求解析。
Request对象的核心功能是request.data属性，

'''

'''
包装器
1.用于基于函数视图的@api_view装饰器
2.用于基于类视图的APIView类
'''
# @api_view(['GET','POST'])
# def snippet_list(request):
#     '''
#     列出所有的snippets，或者创建一个新的snippet
#     '''
#     if request.method == 'GET': # 序列化
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True) # many = True 列表形式
#         return Response(serializer.data)
#     elif request.method == 'POST': # 反序列化
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk):
#     '''
#     获取，更新或删除一个snippet对象
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''
使用基于类的视图重写我们的API
'''
from rest_framework.views import APIView
from django.http import Http404

# class SnippetList(APIView):
#
#     def get(self,request,format = None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet,many = True)
#         return Response(serializer.data)
#
#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#
#     def get_object(self,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Http404
#
#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import mixins
from rest_framework import generics

'''
使用混合（mixins）
使用基于类视图的最大优势之一是它可以轻松地创建可复用的行为。

到目前为止，我们使用的创建/获取/更新/删除操作和我们创建的任何基于模型的API视图非常相似。
这些常见的行为是在REST框架的mixin类中实现的。
'''
# 使用混合mixin
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView
#                   ):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request=request,*args, **kwargs)
#
#     def post(self,request, *args , **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self,request, *args, **kwargs):
#         return self.update(request, *args,**kwargs)
#
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(request,*args,**kwargs)

'''使用通用的基于类的视图
通过使用mixin类，我们使用更少的代码重写了这些视图，但我们还可以再进一步。REST框架提供了一组已经混合好（mixed-in）的通用视图'''

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


from django.contrib.auth.models import User
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request,format=None):
    '''
    1.使用rest_framework 的reverse功能来返回完全限定的URL
    2.URL模式是通过方便的名称来标识的，我们稍后将在snippets/urls.py中声明
    '''
    return Response({
        'user': reverse('user-list',request=request,format=format),
        'snippets': reverse('snippet-list',request=request,format=format)
    })