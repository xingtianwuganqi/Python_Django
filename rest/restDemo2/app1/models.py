
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

'''
contenttype
'''
class Course(models.Model):
    '''
    普通课程
    '''
    title = models.CharField(max_length=32)
    # 仅用于反向查找，不生成数据库
    price_policy_list = GenericRelation('PricePolicy')

class DegreeCourse(models.Model):
    '''
    学位课程
    '''
    title = models.CharField(max_length=32)
    price_policy_list = GenericRelation('PricePolicy')



class PricePolicy(models.Model):
    '''
    价格策略
    '''
    price = models.IntegerField()
    period = models.IntegerField()

    # table_name = models.CharField(verbose_name='关联的表名称')
    # object_id = models.CharField(verbose_name='关联的表中的数据行的ID')

    content_type = models.ForeignKey(ContentType,verbose_name='关联的表名称')
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')

    # 帮助你快速实现content_type操作
    content_object= GenericForeignKey('content_type','object_id')

'''
# 1.为学位课'python全栈'添加一个价格策略：一个月9.9
obj = DegreeCourse.objects.filter(title='Python全栈').first()
# 获取id obj.id
cobj = ContentType.objects.filter(models='course').first()
# 获取id cobj.id
PricePolicy.objects.create(price='9.9',period='30',conent_type_id=cobj,object_id = obj.id)

'''
# # 完全可以用这一句实现
# objc = DegreeCourse.objects.filter(title = 'Python全栈').first()
# PricePolicy.objects.create(price=9.9,period=30,content_type=objc)
