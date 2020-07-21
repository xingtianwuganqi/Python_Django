from rest_framework import serializers
from django.contrib.auth.models import User
from .models import dongzuopian

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')


class DongzuopianSerializers(serializers.ModelSerializer):
    class Meta:
        model = dongzuopian
        fields = ('id','movie_type','movie_name','movie_star','movie_actor','movie_url','movie_img')



