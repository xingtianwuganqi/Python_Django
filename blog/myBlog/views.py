from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Article,Category,Link,Tui,Tag,Banner
# 分页插件包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def hello(request):
#     return HttpResponse('欢迎使用django！')
#
# def index(request):
#     # 添加两个变量，并给它们赋值
#     sitename = 'Django 中文网'
#     url = 'www.django.cn'
#     # 新加一个列表
#     list = [
#         '开发前的准备',
#         '项目需求分析',
#         '数据库设计分析',
#         '创建项目',
#         '基础配置',
#         '欢迎页面',
#         '创建数据库模型',
#     ]
#     # 在来的基础上新加一个字典
#     mydict = {
#         'name': '吴秀峰',
#         'qq': '445813',
#         'wx': 'vipdjango',
#         'email': '445813@qq.com',
#         'Q群': '10218442',
#     }
#     # 把两个变量封装到上下文里
#     context = {
#         'sitename': sitename,
#         'url': url,
#         'list':list,
#         'mydict': mydict,
#     }
#     # 把上下文传递到模板里
#     return render(request,'index.html',context)
#
#
# def articleList(request):
#     #对Article进行声明并实例化，然后生成对象allarticle
#
#     article = Article.objects.all()
#
#     #把查询到的对象，封装到上下文
#     context = {
#         'allarticle': article,
#     }
#     return render(request,'allarticle.html',context)



def index(request):
    allcategory = Category.objects.all()
    # 查询banner
    banner = Banner.objects.filter(is_active=True)[0:4]
    # 首页推荐
    tui = Article.objects.all().filter(tui_id = 1)[0:3]
    # 首页最新文章推荐
    allarticle = Article.objects.all().order_by('-id')[0:10]
    # 热门
    hot = Article.objects.all().order_by('views')[:10]
    # 热门推荐
    remen = Article.objects.all().filter(tui_id = 2)[0:4]

    # 标签
    tags = Tag.objects.all()
    # 友情链接
    link = Link.objects.all()
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags' : tags,
        'link' : link
    }
    return render(request,'index.html',context)

def list(request,lid):

    list = Article.objects.all().filter(category_id = lid) # 获取通过url传过来的lid，然后筛选出文章
    cname = Category.objects.all().get(id = lid) #获取当前文章的栏目名
    remen = Article.objects.all().filter(tui_id = 2)[:6] # 获取热门推荐
    allcategory = Category.objects.all() # 导航所有分类
    tags = Tag.objects.all() # 获取所有文章标签

    # 获取页数
    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(list,5)#对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容


    #   locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典。
    #
    #
    return render(request,'list.html',locals())

def show(request,sid):
    show = Article.objects.all().get(id = sid)
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.all().filter(tui_id = 2)[: 6]
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(create_time__gt=show.create_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=show.create_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request,'show.html',locals())

def tag(request,tag):

    list = Article.objects.filter(tag__name=tag)  # 通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

def search(request):
    pass

def about(request):
    pass












