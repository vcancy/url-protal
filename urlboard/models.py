#coding=utf-8
from django.db import models

# Create your models here.

class Group(models.Model):
    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组'
    name = models.CharField(max_length=200,verbose_name = "名称")
    desc = models.CharField(max_length=200,verbose_name = "描述",blank=True)
    pub_date = models.DateTimeField(verbose_name = "创建日期",auto_now_add=True)

    def __unicode__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name
class URL(models.Model):
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URL'
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="分组")
    name = models.CharField(max_length=200,verbose_name = "名称")
    url = models.CharField(max_length=200,verbose_name = "URL")
    desc = models.CharField(max_length=200,verbose_name = "描述")

    def __unicode__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.name