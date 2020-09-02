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
from .serializers import SnippetSerializer

'''
REST 框架引入乐乐一个扩展了常规HttpRequest的Request对象，并提供了更灵活的请求解析。
Request对象的核心功能是request.data属性，

'''

'''
包装器
1.用于基于函数视图的@api_view装饰器
2.用于基于类视图的APIView类
'''
@api_view(['GET','POST'])
def snippet_list(request):
    '''
    列出所有的snippets，或者创建一个新的snippet
    '''
    if request.method == 'GET': # 序列化
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True) # many = True 列表形式
        return Response(serializer.data)
    elif request.method == 'POST': # 反序列化
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk):
    '''
    获取，更新或删除一个snippet对象
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















