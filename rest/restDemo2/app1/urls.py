from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url

urlpatterns = [
    url(r'^test/$',views.test)
]