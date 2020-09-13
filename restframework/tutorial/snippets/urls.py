from django.conf.urls import url
from . import views
from django.conf.urls import include
# urlpatterns = [
#     url(r'^snippets/$',views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail)
# ]

urlpatterns = [
    url(r'^snippets/$',views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
    # 获取用户信息
    url(r'^users/$',views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]