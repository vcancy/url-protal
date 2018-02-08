# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class TErpMerchantInfo(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    coordinate = models.CharField(max_length=50, blank=True, null=True)
    customer = models.CharField(max_length=200, blank=True, null=True)
    industy = models.CharField(max_length=10, blank=True, null=True)
    linker = models.CharField(max_length=50, blank=True, null=True)
    linkerposition = models.CharField(db_column='linkerPosition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linkerphone = models.CharField(db_column='linkerPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=50, blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    salesdept = models.CharField(db_column='salesDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salesman = models.CharField(db_column='salesMan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    endeddate = models.DateField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_ERP_MERCHANT_INFO'


class TMerchant(models.Model):
    cusnm = models.CharField(db_column='CUSNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjnm = models.CharField(db_column='PRJNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctyno = models.CharField(db_column='CTYNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cutype = models.CharField(db_column='CUTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salnm = models.CharField(db_column='SALNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    depnm = models.CharField(db_column='DEPNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prono = models.CharField(db_column='PRONO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pronm = models.CharField(db_column='PRONM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    floginnm = models.CharField(db_column='FLOGINNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fstartdate = models.DateTimeField(db_column='FSTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fendeddate = models.DateTimeField(db_column='FENDEDDATE', blank=True, null=True)  # Field name made lowercase.
    fstatus = models.CharField(db_column='FSTATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MERCHANT'


class TMerchant66Fe0422815F11E7B531Acbc32Bf74C3(models.Model):
    cusnm = models.CharField(db_column='CUSNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjnm = models.CharField(db_column='PRJNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctyno = models.CharField(db_column='CTYNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cutype = models.CharField(db_column='CUTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salnm = models.CharField(db_column='SALNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    depnm = models.CharField(db_column='DEPNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prono = models.CharField(db_column='PRONO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pronm = models.CharField(db_column='PRONM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    floginnm = models.CharField(db_column='FLOGINNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fstartdate = models.DateTimeField(db_column='FSTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fendeddate = models.DateTimeField(db_column='FENDEDDATE', blank=True, null=True)  # Field name made lowercase.
    fstatus = models.CharField(db_column='FSTATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MERCHANT66fe0422815f11e7b531acbc32bf74c3'


class TMerchant7Dcb6Fcc815B11E7B8E1Acbc32Bf74C3(models.Model):
    cusnm = models.CharField(db_column='CUSNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjnm = models.CharField(db_column='PRJNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctyno = models.CharField(db_column='CTYNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cutype = models.CharField(db_column='CUTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salnm = models.CharField(db_column='SALNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    depnm = models.CharField(db_column='DEPNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prono = models.CharField(db_column='PRONO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pronm = models.CharField(db_column='PRONM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    floginnm = models.CharField(db_column='FLOGINNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fstartdate = models.DateTimeField(db_column='FSTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fendeddate = models.DateTimeField(db_column='FENDEDDATE', blank=True, null=True)  # Field name made lowercase.
    fstatus = models.CharField(db_column='FSTATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MERCHANT7dcb6fcc815b11e7b8e1acbc32bf74c3'


class TMerchantManager(models.Model):
    account = models.CharField(max_length=50, blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dingtalkid = models.CharField(db_column='dingTalkId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dingtalkname = models.CharField(db_column='dingTalkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_MERCHANT_MANAGER'


class TMerchantManagerCopy(models.Model):
    account = models.CharField(max_length=50, blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dingtalkid = models.CharField(db_column='dingTalkId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dingtalkname = models.CharField(db_column='dingTalkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_MERCHANT_MANAGER_copy'


class TMerchantCopy(models.Model):
    cusnm = models.CharField(db_column='CUSNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prjnm = models.CharField(db_column='PRJNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctyno = models.CharField(db_column='CTYNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cutype = models.CharField(db_column='CUTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salnm = models.CharField(db_column='SALNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    depnm = models.CharField(db_column='DEPNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prono = models.CharField(db_column='PRONO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pronm = models.CharField(db_column='PRONM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    floginnm = models.CharField(db_column='FLOGINNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fstartdate = models.DateTimeField(db_column='FSTARTDATE', blank=True, null=True)  # Field name made lowercase.
    fendeddate = models.DateTimeField(db_column='FENDEDDATE', blank=True, null=True)  # Field name made lowercase.
    fstatus = models.CharField(db_column='FSTATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_MERCHANT_copy'


class TReportLog(models.Model):
    app = models.CharField(max_length=20, blank=True, null=True)
    log = models.CharField(max_length=2000, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_LOG'


class TReportMemberDailyCalcLog(models.Model):
    account = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMBER_DAILY_CALC_LOG'


class TReportMemberNewCustInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    organization_account = models.CharField(max_length=20, blank=True, null=True)
    new_cust_cnt = models.IntegerField(blank=True, null=True)
    new_consumer_cnt = models.IntegerField(blank=True, null=True)
    new_store_cnt = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMBER_NEW_CUST_INFO'


class TReportMemberNewCustTotal(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    organization_account = models.CharField(max_length=20, blank=True, null=True)
    new_cust_cnt = models.IntegerField(blank=True, null=True)
    new_consumer_cnt = models.IntegerField(blank=True, null=True)
    new_store_cnt = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMBER_NEW_CUST_TOTAL'


class TReportMemberRankInfo(models.Model):
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    level_name = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMBER_RANK_INFO'


class TReportMemberTransactionDailyInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    organization_account = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    transaction_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_cnt = models.IntegerField(blank=True, null=True)
    store_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coupon_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gift_coupon_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reward_points = models.IntegerField(blank=True, null=True)
    store_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_cnt = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMBER_TRANSACTION_DAILY_INFO'


class TReportMemeberTransactionTotal(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    organization_account = models.CharField(max_length=20, blank=True, null=True)
    transaction_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_cnt = models.IntegerField(blank=True, null=True)
    store_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coupon_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gift_coupon_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reward_points = models.IntegerField(blank=True, null=True)
    store_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store_cnt = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_REPORT_MEMEBER_TRANSACTION_TOTAL'


class TTaskInfo(models.Model):
    appcode = models.CharField(max_length=20, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    metabase = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_TASK_INFO'


class TTaskUnsubscibe(models.Model):
    appcode = models.CharField(max_length=20, blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=50, blank=True, null=True)
    dingtalkid = models.CharField(max_length=50, blank=True, null=True)
    dingtalkname = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_TASK_UNSUBSCIBE'


class TTaskUnsubscribeLog(models.Model):
    dingtalkname = models.CharField(db_column='dingTalkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dingtalkid = models.CharField(db_column='dingTalkId', max_length=50)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_TASK_UNSUBSCRIBE_LOG'


class Wxbmemberactionrecordbo(models.Model):
    time = models.CharField(max_length=255, blank=True, null=True)
    sn = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    vipid = models.IntegerField(blank=True, null=True)
    actiondate = models.CharField(max_length=255, blank=True, null=True)
    customername = models.CharField(max_length=255, blank=True, null=True)
    organizationaccount = models.CharField(max_length=255, blank=True, null=True)
    merchantaccount = models.CharField(max_length=255, blank=True, null=True)
    merchantname = models.CharField(max_length=255, blank=True, null=True)
    ordercode = models.CharField(max_length=255, blank=True, null=True)
    customerid = models.CharField(max_length=255, blank=True, null=True)
    merchantid = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(max_length=255, blank=True, null=True)
    actiontype = models.IntegerField(blank=True, null=True)
    headimgurl = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    organizationname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WxbMemberActionRecordBo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TAdvanceorderNewBaseSelf(models.Model):
    vendorshopid = models.CharField(max_length=100, blank=True, null=True)
    referorderid = models.CharField(max_length=100, blank=True, null=True)
    advanceorderid = models.CharField(max_length=100, blank=True, null=True)
    customerid = models.CharField(max_length=100, blank=True, null=True)
    itemid = models.CharField(max_length=100, blank=True, null=True)
    itemname = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    lasttime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advanceorder_new_base_self'


class TDatareportConfig(models.Model):
    task = models.CharField(max_length=255, verbose_name="任务编号")
    sqltext = models.TextField(max_length=1000, verbose_name="sql脚本")
    attach = models.IntegerField(verbose_name="是否添加附件excel.1-是，0-否",default=1)
    receivers = models.CharField(max_length=1000, verbose_name="接受人邮箱，多个已逗号','分隔",default="xxx@guoshengtianfeng.com")
    dbinfo = models.TextField(max_length=255, verbose_name='数据库',default='{"host":"192.168.103.201","user":"root","pwd":"Wxb123456!","port":3306,"db":"report"}')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="邮件标题")
    updatetime = models.DateTimeField(blank=True, null=True, verbose_name="更新时间",auto_now = True)

    class Meta:
        verbose_name = 'rws-定时邮件发送任务'
        verbose_name_plural = 'rws-定时邮件发送任务'
        managed = True
        db_table = 't_datareport_config'
    def __str__(self):  # admin后台显示的描述，以及python 对象的名称
        return self.task

class TErpDeviceInfo(models.Model):
    saler_name = models.CharField(max_length=255, blank=True, null=True)
    saler_number = models.CharField(max_length=255, blank=True, null=True)
    cust_name = models.CharField(max_length=255, blank=True, null=True)
    return_num = models.IntegerField(blank=True, null=True)
    total_num = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    eid = models.CharField(max_length=255, blank=True, null=True)
    updatedate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_erp_device_info'


class TErpMerchantInfo(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    coordinate = models.CharField(max_length=50, blank=True, null=True)
    customer = models.CharField(max_length=200, blank=True, null=True)
    industy = models.CharField(max_length=10, blank=True, null=True)
    linker = models.CharField(max_length=50, blank=True, null=True)
    linkerposition = models.CharField(db_column='linkerPosition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linkerphone = models.CharField(db_column='linkerPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=50, blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    salesdept = models.CharField(db_column='salesDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salesman = models.CharField(db_column='salesMan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    endeddate = models.DateField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_erp_merchant_info'


class TReportAnnualAccountInfo(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    has_market = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_annual_account_info'


class TReportAnnualMerchant2017(models.Model):
    merchant_account = models.CharField(max_length=255, blank=True, null=True)
    merchant_name = models.CharField(max_length=255, blank=True, null=True)
    has_market_activity = models.IntegerField(blank=True, null=True)
    fisrt_order = models.DateTimeField(blank=True, null=True)
    first_activity = models.DateTimeField(blank=True, null=True)
    first_coupon = models.DateTimeField(blank=True, null=True)
    tablecard_login = models.IntegerField(blank=True, null=True)
    phone_total = models.IntegerField(blank=True, null=True)
    phone_in_cnt = models.IntegerField(blank=True, null=True)
    phone_game_cnt = models.IntegerField(blank=True, null=True)
    phone_activity_cnt = models.IntegerField(blank=True, null=True)
    order_cnt = models.IntegerField(blank=True, null=True)
    paper = models.FloatField(blank=True, null=True)
    customer_total_cnt = models.IntegerField(blank=True, null=True)
    old_customer_rate = models.FloatField(blank=True, null=True)
    lively_customer_cnt = models.IntegerField(blank=True, null=True)
    silent_customer_cnt = models.IntegerField(blank=True, null=True)
    loss_customer_cnt = models.IntegerField(blank=True, null=True)
    coupon_total = models.IntegerField(blank=True, null=True)
    coupon_use = models.IntegerField(blank=True, null=True)
    coupon_conversion_rate = models.FloatField(blank=True, null=True)
    gamer_total = models.IntegerField(blank=True, null=True)
    gamer_top_cnt = models.IntegerField(blank=True, null=True)
    customer_obtain_rate = models.FloatField(blank=True, null=True)
    popular_customer_name = models.CharField(max_length=255, blank=True, null=True)
    popular_customer_phone = models.CharField(max_length=255, blank=True, null=True)
    popular_customer_custtimes = models.IntegerField(blank=True, null=True)
    popular_customer_amount = models.IntegerField(blank=True, null=True)
    best_day_date = models.DateField(blank=True, null=True)
    best_day_amt = models.FloatField(blank=True, null=True)
    lowest_day_date = models.DateField(blank=True, null=True)
    lowest_day_amt = models.FloatField(blank=True, null=True)
    over_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_annual_merchant_2017'


class TReportAnnualMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    subtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_annual_message'


class TReportAnnualOrganization2017(models.Model):
    orginazition_account = models.CharField(max_length=255, blank=True, null=True)
    orginazition_name = models.CharField(max_length=255, blank=True, null=True)
    fisrt_order = models.DateTimeField(blank=True, null=True)
    first_activity = models.DateTimeField(blank=True, null=True)
    first_coupon = models.DateTimeField(blank=True, null=True)
    tablecard_login = models.IntegerField(blank=True, null=True)
    phone_total = models.IntegerField(blank=True, null=True)
    phone_in_cnt = models.IntegerField(blank=True, null=True)
    phone_game_cnt = models.IntegerField(blank=True, null=True)
    phone_activity_cnt = models.IntegerField(blank=True, null=True)
    order_cnt = models.IntegerField(blank=True, null=True)
    paper = models.FloatField(blank=True, null=True)
    customer_total_cnt = models.IntegerField(blank=True, null=True)
    old_customer_rate = models.FloatField(blank=True, null=True)
    lively_customer_cnt = models.IntegerField(blank=True, null=True)
    silent_customer_cnt = models.IntegerField(blank=True, null=True)
    loss_customer_cnt = models.IntegerField(blank=True, null=True)
    coupon_total = models.IntegerField(blank=True, null=True)
    coupon_use = models.IntegerField(blank=True, null=True)
    gamer_total = models.IntegerField(blank=True, null=True)
    gamer_top_cnt = models.IntegerField(blank=True, null=True)
    coupon_conversion_rate_top1 = models.CharField(max_length=255, blank=True, null=True)
    coupon_conversion_rate_top2 = models.CharField(max_length=255, blank=True, null=True)
    coupon_conversion_rate_top3 = models.CharField(max_length=255, blank=True, null=True)
    customer_active_top1 = models.CharField(max_length=255, blank=True, null=True)
    customer_active_top2 = models.CharField(max_length=255, blank=True, null=True)
    customer_active_top3 = models.CharField(max_length=255, blank=True, null=True)
    customer_obtain_rate_top1 = models.CharField(max_length=255, blank=True, null=True)
    customer_obtain_rate_top2 = models.CharField(max_length=255, blank=True, null=True)
    customer_obtain_rate_top3 = models.CharField(max_length=255, blank=True, null=True)
    customer_obtain_rate_top1_customer_cnt = models.IntegerField(blank=True, null=True)
    has_market_activity = models.IntegerField(blank=True, null=True)
    customer_obtain_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_annual_organization_2017'


class TReportAnnualSubmit(models.Model):
    account = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    love = models.IntegerField(blank=True, null=True)
    subtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_annual_submit'


class TReportDauDaily(models.Model):
    account_name = models.CharField(max_length=255, blank=True, null=True)
    dau = models.FloatField(blank=True, null=True)
    bind_device_cnt = models.IntegerField(blank=True, null=True)
    table_login_cnt = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    updatedate = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_dau_daily'


class TReportMemberSignCnt(models.Model):
    vip_id = models.IntegerField(blank=True, null=True)
    organization_account = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    sign_total = models.IntegerField(blank=True, null=True)
    old_sign_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_member_sign_cnt'


class TReportMemberStoreConsumeAmt(models.Model):
    vip_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    recharge_amt = models.FloatField(blank=True, null=True)
    consume_amt = models.FloatField(blank=True, null=True)
    recharge_consume_amt = models.FloatField(blank=True, null=True)
    cash_consume_amt = models.FloatField(blank=True, null=True)
    organization_account = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_member_store_consume_amt'


class TReportMemberStoreConsumeCnt(models.Model):
    vip_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    recharge_cnt = models.IntegerField(blank=True, null=True)
    consume_cnt = models.IntegerField(blank=True, null=True)
    organization_account = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_member_store_consume_cnt'


class TReportMemberVipCustomer(models.Model):
    vip_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=32, blank=True, null=True)
    organization_account = models.CharField(max_length=20, blank=True, null=True)
    merchant_account = models.CharField(max_length=20, blank=True, null=True)
    register_time = models.DateTimeField()
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    cell_phone = models.CharField(max_length=11, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    sign_total = models.IntegerField()
    level_id = models.IntegerField(blank=True, null=True)
    is_validate = models.IntegerField(blank=True, null=True)
    last_consume_date = models.DateTimeField(blank=True, null=True)
    last_sign_date = models.DateTimeField(blank=True, null=True)
    openid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    give_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    principal_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    vip_create_date = models.DateTimeField(blank=True, null=True)
    vip_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_member_vip_customer'


class TStatWxbmemberactionrecordbo(models.Model):
    updatetime = models.DateTimeField(blank=True, null=True)
    merchantname = models.CharField(db_column='merchantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vipid = models.BigIntegerField(db_column='vipId', blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='merchantId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    xxx = models.BigIntegerField(blank=True, null=True)
    merchantaccount = models.CharField(db_column='merchantAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.CharField(db_column='headImgUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    organizationname = models.CharField(db_column='organizationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordercode = models.CharField(db_column='orderCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actiondate = models.BigIntegerField(db_column='actionDate', blank=True, null=True)  # Field name made lowercase.
    sn = models.CharField(max_length=255, blank=True, null=True)
    customerid = models.CharField(db_column='customerId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organizationaccount = models.CharField(db_column='organizationAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actiontype = models.BigIntegerField(db_column='actionType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stat_WxbMemberActionRecordBo'


class TStatMemberVipinfo(models.Model):
    realityconsumenumber = models.BigIntegerField(db_column='RealityConsumeNumber', blank=True, null=True)  # Field name made lowercase.
    realityrechargenumber = models.BigIntegerField(db_column='RealityRechargeNumber', blank=True, null=True)  # Field name made lowercase.
    realityselfconsumenumber = models.BigIntegerField(db_column='RealitySelfConsumeNumber', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=255, blank=True, null=True)
    realityselfrechargenumber = models.BigIntegerField(db_column='RealitySelfRechargeNumber', blank=True, null=True)  # Field name made lowercase.
    realityconsumesum = models.FloatField(db_column='RealityConsumeSum', blank=True, null=True)  # Field name made lowercase.
    registeramount = models.BigIntegerField(db_column='RegisterAmount', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)
    realityrechargesum = models.FloatField(db_column='RealityRechargeSum', blank=True, null=True)  # Field name made lowercase.
    merchant_account = models.CharField(max_length=255, blank=True, null=True)
    newaddamount = models.BigIntegerField(db_column='NewAddAmount', blank=True, null=True)  # Field name made lowercase.
    time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_member_vipinfo'


class TStatPayDayweektrend(models.Model):
    table_cnt = models.BigIntegerField(blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)
    total_cnt = models.BigIntegerField(blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    table_total_cnt = models.BigIntegerField(blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_pay_dayweektrend'


class WxbMerchantAnnualReport2017(models.Model):
    merchant_account = models.CharField(max_length=255, blank=True, null=True)
    merchant_name = models.CharField(max_length=255, blank=True, null=True)
    orginazition_account = models.CharField(max_length=255, blank=True, null=True)
    orginazition_name = models.CharField(max_length=255, blank=True, null=True)
    first_order_date = models.DateTimeField(blank=True, null=True)
    first_coupon_date = models.CharField(max_length=255, blank=True, null=True)
    login_cnt = models.IntegerField(blank=True, null=True)
    customer_cnt = models.IntegerField(blank=True, null=True)
    customer_phonein_cnt = models.IntegerField(blank=True, null=True)
    customer_game_cnt = models.IntegerField(blank=True, null=True)
    customer_tablecard_cnt = models.IntegerField(blank=True, null=True)
    order_cnt = models.IntegerField(blank=True, null=True)
    paper_cnt = models.FloatField(blank=True, null=True)
    old_customer_cnt = models.IntegerField(blank=True, null=True)
    old_customer_percent = models.FloatField(blank=True, null=True)
    customer_activity_percent = models.FloatField(blank=True, null=True)
    customer_activity_rank = models.IntegerField(blank=True, null=True)
    coupon_cnt = models.IntegerField(blank=True, null=True)
    coupon_use = models.IntegerField(blank=True, null=True)
    coupon_switch_percent = models.FloatField(blank=True, null=True)
    conpon_switch_rank = models.FloatField(blank=True, null=True)
    gamer_total = models.IntegerField(blank=True, null=True)
    gamer_play_cnt = models.IntegerField(blank=True, null=True)
    customer_obtain_percent = models.FloatField(blank=True, null=True)
    customer_obtain_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wxb_merchant_annual_report_2017'
