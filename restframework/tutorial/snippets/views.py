from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

class JSONResponse(HttpResponse):

    def __init__(self,data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt # 请注意，因为我们希望能够从不具有CSRF令牌的客户端对此视图进行post，因此我们需要将视图标记为csrf_exempt
def snippet_list(request):
    '''
    列出所有的code snippet,或创建一个新的snippet
    '''
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)


@csrf_exempt
def snippet_detail(request,pk):
    '''
    获取、更新、或删除一个 code snippet
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=400)

