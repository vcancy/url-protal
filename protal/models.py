from django.db import models

# Create your models here.
class DatabaseType(models.Model):
    class Meta:
        verbose_name = '数据库类型'
        verbose_name_plural = '数据库类型'
    name = models.CharField(max_length=200,verbose_name = "名称")
    desc = models.CharField(max_length=200,verbose_name = "描述",blank=True)
    pub_date = models.DateTimeField(verbose_name = "创建日期",auto_now_add=True)

    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name

class Database(models.Model):
    class Meta:
        verbose_name = '数据库名称'
        verbose_name_plural = '数据库名称'
    name = models.CharField(max_length=200,verbose_name = "名称")
    type = models.ForeignKey(DatabaseType, on_delete=models.CASCADE,verbose_name = "类型")
    desc = models.CharField(max_length=200,verbose_name = "描述",blank=True)
    pub_date = models.DateTimeField(verbose_name = "创建日期",auto_now_add=True)
    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name

class FunctionCode(models.Model):
    class Meta:
        verbose_name = '方法类型'
        verbose_name_plural = '方法类型'
    name = models.CharField(max_length=200,verbose_name = "名称")
    code = models.CharField(max_length=200, verbose_name="编号")
    desc = models.CharField(max_length=200,verbose_name = "描述",blank=True)
    pub_date = models.DateTimeField(verbose_name = "创建日期",auto_now_add=True)

    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name

class Function(models.Model):
    class Meta:
        verbose_name = '查询信息'
        verbose_name_plural = '查询信息'
    funcode = models.ForeignKey(FunctionCode,on_delete=models.CASCADE,verbose_name = "方法类型")
    name = models.CharField(max_length=200,verbose_name = "名称")
    content = models.CharField(max_length=200,verbose_name = "执行查询内容：表，视图，存储过程")
    para = models.CharField(max_length=200,blank=True,verbose_name = "参数")
    desc = models.CharField(max_length=200,verbose_name = "描述")
    limit = models.IntegerField(default=10,verbose_name="页面展示数量")
    dataase = models.ForeignKey(Database, on_delete=models.CASCADE,verbose_name="数据库名称")
    output = models.CharField(max_length=200,default='',verbose_name = "输出字段")
    pub_date = models.DateTimeField(verbose_name = "创建日期",auto_now_add=True)

    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name

class platfromApiJson:
    def __init__(self,**kwargs):
        self.funcode = kwargs['funcode']
        self.database = kwargs['database']
        self.fun = kwargs['fun']
        self.para = kwargs['para']
        self.limit = kwargs['limit']
        self.output = kwargs['output']

    def convert_to_dict(self):
        '''把Object对象转换成Dict对象'''
        dict = {}
        dict.update(self.__dict__)
        return dict