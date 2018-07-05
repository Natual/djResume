# _*_ coding=utf-8 _*_
from django.db import models


# Create your models here.
class pay_user(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', primary_key=True)
    open_id = models.CharField(verbose_name='微信的openid', max_length=36, blank=True, null=True)
    name = models.CharField(verbose_name='姓名', max_length=10)
    mobile = models.CharField(verbose_name='手机号码',max_length=12)
    idCard = models.CharField(verbose_name='身份证号码', max_length=20, blank=True, null=True)
    staff = models.CharField(verbose_name='职务职级', max_length=16, blank=True, null=True)
    staffNo = models.CharField(verbose_name='员工编号', max_length=20, blank=True, null=True)
    depart = models.CharField(verbose_name='党支部名称', max_length=100)
    createTime = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        verbose_name = '党员信息'
        verbose_name_plural =  '党员信息'

    def __str__(self):
        return self.name


class fee(models.Model):
    payId = models.IntegerField(verbose_name='费用ID', primary_key=True)
    userid = models.ForeignKey(pay_user, on_delete=models.CASCADE, verbose_name='用户ID')
    monthlyFee = models.DecimalField(verbose_name='每月缴纳金额', max_digits=7, decimal_places=2)
    feeDone = models.DecimalField(verbose_name='当期已缴纳的金额', max_digits=7, decimal_places=2)
    feeOwn = models.DecimalField(verbose_name='当期仍需交纳的金额', max_digits=7, decimal_places=2)
    month = models.CharField(verbose_name='当期所属的月份', max_length=8)
    payMethod = models.IntegerField(verbose_name='缴纳方式：1=按月缴纳，3=按季度缴纳，12=按年缴纳')
    status = models.IntegerField(verbose_name='当期缴纳状态: 0= 未缴纳完毕，1= 已缴纳完毕')
    createTime = models.DateTimeField(verbose_name='创建时间')
    updateTime = models.DateTimeField(verbose_name='更新时间')
    order = models.CharField(verbose_name='订单号', max_length=32, default='',blank=True, null=True)

    class Meta:
        verbose_name = '缴费信息'
        verbose_name_plural = '缴费信息'

    def __str__(self):
        return '缴费信息'


class recharge_oder(models.Model):
    total_fee = models.DecimalField(verbose_name='订单金额', max_digits=7, decimal_places=2)
    out_trade_no = models.CharField(verbose_name='自主生成的订单号', max_length=32)
    payjs_order_id = models.CharField(verbose_name='payjs 的订单号', max_length=32)
    transaction_id = models.CharField(verbose_name='微信用户手机显示的订单号', max_length=32)
    time_end = models.CharField(verbose_name='支付成功时间', max_length=32)
    openid = models.CharField(verbose_name='用户OPENID标志', max_length=64)
    attach = models.CharField(verbose_name='用户自定义数据', max_length=250, blank=True, null=True)
    mchid = models.CharField(verbose_name='payjs 商户号', max_length=24)
    create_time = models.DateTimeField(verbose_name='创建时间',  auto_now_add=True)

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'

    def __str__(self):
        return self.out_trade_no
