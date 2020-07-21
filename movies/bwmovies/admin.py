from django.contrib import admin

from .models import dongzuopian

@admin.register(dongzuopian)
class dongzuopianAdmin(admin.ModelAdmin):

    # 要显示的字段
    list_display = ['id','movie_type','movie_name','movie_star','movie_actor','movie_url','movie_img']
    # 分页
    list_per_page = 50
