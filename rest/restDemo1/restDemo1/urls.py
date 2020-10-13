"""restDemo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls import url,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('^users/$',views.users),
    # url('^students/$', views.studentsView.as_view()),
    # url('^get_order/$', views.get_order),
    # url('^del_order/$', views.del_order),
    # url('^update_order/$', views.update_order),
    # url('^dog/$',views.DogView.as_view())

    url(r'^admin/$',admin.site.urls),
    url(r'^api/v1/auth/$',views.AnthView.as_view()),
    url(r'^api/v1/register/$',views.UserView.as_view()),
    url(r'^api/v1/order/$',views.OrderView.as_view()),

    # 分发
    url(r'^api/',include('app1.urls'))
]
