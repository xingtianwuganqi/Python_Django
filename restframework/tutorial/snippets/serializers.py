from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
#
#     def create(self, validated_data):
#         '''
#         根据提供的验证过的数据创建并返回一个新的'snippet'实例
#         '''
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         '''
#         根据提供的验证过的数据更新和返回一个已经存在的'Snippet'实例
#         '''
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.linenos = validated_data.get('linenos',instance.linenos)
#         instance.language = validated_data.get('language',instance.language)
#         instance.style = validated_data.get('style',instance.style)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer 类并不会做任何特别神奇的事情，它们只是创建序列化器类的快捷方式
    1.一组自动确定的字段
    2.默认简单实现的create()和update()方法
    '''
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style')

'''
创建一个新的序列化器

因为'snippets' 在用户模型中是一个反向关联关系。在使用 ModelSerializer 类时它默认不会被包含，
所以我们需要为它添加一个显式字段。
'''
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        field = ('id','username','snippets','owner')