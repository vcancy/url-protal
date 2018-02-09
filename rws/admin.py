from django.contrib import admin
from .models import TDatareportConfig
# Register your models here.

class rwsAdmin(admin.ModelAdmin):
    list_display = ('task','title','enable','schedule','receivers') #添加字段显示
    search_fields = ('task','title') #添加快速查询栏

admin.site.register(TDatareportConfig,rwsAdmin)