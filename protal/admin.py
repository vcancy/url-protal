from django.contrib import admin
from .models  import Function,Database,DatabaseType,FunctionCode
# Register your models here.
admin.site.register(Function)
admin.site.register(Database)
admin.site.register(DatabaseType)
admin.site.register(FunctionCode)