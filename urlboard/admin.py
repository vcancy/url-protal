from django.contrib import admin
from .models import URL,Group
# Register your models here.
class urlAdmin(admin.ModelAdmin):
    list_display = ('name','group','url','desc') #添加字段显示
    search_fields = ('name') #添加快速查询栏
admin.site.register(URL,urlAdmin)
admin.site.register(Group)