from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializers , DongzuopianSerializers
from .models import dongzuopian

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class DongzuopianViewSet(viewsets.ModelViewSet):
    queryset = dongzuopian.objects.all()
    serializer_class = DongzuopianSerializers
