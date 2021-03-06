from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url

urlpatterns = [
    url(r'^users/$',views.users),
    url(r'^(?P<version>[v1|v2]+)/user/$',views.UsersView.as_view(),name='uuu'),
    url(r'^(?P<version>[v1|v2]+)/django/$', views.DjangoView.as_view(), name='ddd'),
    url(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/group/(?P<pk>\d+)$', views.GroupView.as_view(),name='gp'), #name 别名


    url(r'^(?P<version>[v1|v2]+)/v1/$', views.View1View.as_view()),  # name 别名

]