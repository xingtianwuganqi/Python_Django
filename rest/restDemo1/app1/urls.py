from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url

urlpatterns = [
    url(r'^users/$',views.users),
    url(r'^(?P<version>[v1|v2]+)/user/$',views.UsersView.as_view(),name='uuu'),
    url(r'^(?P<version>[v1|v2]+)/django/$', views.DjangoView.as_view(), name='ddd')

]