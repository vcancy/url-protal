# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
class TDatareportConfig(models.Model):
    task = models.CharField(max_length=255, verbose_name="任务编号")
    sqltext = models.TextField(max_length=1000, verbose_name="sql脚本")
    attach = models.IntegerField(verbose_name="是否添加附件excel.1-是，0-否",default=1)
    receivers = models.CharField(max_length=1000, verbose_name="接受人邮箱，多个已逗号','分隔",default="xxx@guoshengtianfeng.com")
    dbinfo = models.TextField(max_length=255, verbose_name='数据库',default='{"host":"192.168.103.201","user":"root","pwd":"Wxb123456!","port":3306,"db":"report"}')
    title = models.CharField(max_length=255, blank=False, null=True, verbose_name="邮件标题")
    updatetime = models.DateTimeField(blank=True, null=False, verbose_name="更新时间",auto_now = True)
    enable = models.IntegerField(blank=True, null=False,verbose_name="是否启用，0-否，1-启用",default=1)
    schedule = models.DateTimeField(blank=True, null=False,verbose_name="任务执行时间")
    class Meta:
        verbose_name = 'rws-定时邮件发送任务'
        verbose_name_plural = 'rws-定时邮件发送任务'
        managed = True
        db_table = 't_datareport_config'
    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.task