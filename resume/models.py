# _*_ coding=utf-8 _*_
from django.db import models

# Create your models here.
class BaseInfo(models.Model):
    name = models.CharField(max_length=5, verbose_name='姓名')
    application = models.CharField(max_length=50, blank=True, null=True, verbose_name='应聘职位')
    applyTime = models.CharField(max_length=20, blank=True, null=True,  verbose_name='申请时间')
    applyCompany = models.CharField(max_length=20, blank=True, null=True, verbose_name='应聘公司')
    match = models.CharField(max_length=5, blank=True, null=True, verbose_name='匹配程度')
    mobile = models.CharField(max_length=24, verbose_name='手机号码')
    email = models.CharField(max_length=30, verbose_name='邮箱')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='居住地')
    status = models.CharField(max_length=20,  blank=True, null=True, verbose_name='求职状态')
    gender = models.CharField(max_length=6, choices=(('Male', '男'), ('Female', '女')), verbose_name='性别')
    birth = models.CharField(max_length=20, blank=True, null=True, verbose_name='出生日期')
    workExperiod = models.CharField(max_length=15, verbose_name='工作经验')
    resumeID = models.CharField(max_length=15,  blank=True, null=True, verbose_name='简历ID')
    resident = models.CharField(max_length=50, blank=True, null=True, verbose_name='户籍')
    income = models.CharField(max_length=50,  blank=True, null=True, verbose_name='目前年收入')
    degree = models.CharField(max_length=10, blank=True, null=True, verbose_name='学历')
    self_evaluation = models.CharField(max_length=250, blank=True, null=True, verbose_name='自我评价')

    class Meta:
        verbose_name = '用户基本信息'
        verbose_name_plural = '用户基本信息'

    def __str__(self):
        return self.name

class wantJob(models.Model):
    baseInfo = models.ForeignKey(BaseInfo, on_delete=models.CASCADE, verbose_name='基本信息', default='1')
    expectSalary = models.CharField(max_length=50,blank=True, null=True, verbose_name='期望薪资')
    address = models.CharField(max_length=20, blank=True, null=True, verbose_name='期望工作地点')
    position = models.CharField(max_length=50, blank=True, null=True, verbose_name='求职岗位')
    busi = models.CharField(max_length=50, blank=True, null=True, verbose_name='期望行业')
    joinTime = models.CharField(max_length=50, blank=True, null=True, verbose_name='到岗时间')
    workType = models.CharField(max_length=20, blank=True, null=True, verbose_name='工作类型')

    class Meta:
        verbose_name = '求职意向'
        verbose_name_plural = '求职意向'

    def __str__(self):
        return '求职意向'


class experience(models.Model):
    baseInfo = models.ForeignKey(BaseInfo, on_delete=models.CASCADE, verbose_name='基本信息', default='1')
    workExperience = models.TextField(verbose_name='工作经验')
    projectExprience = models.TextField(verbose_name='项目经验', blank=True, null=True)
    education = models.TextField(verbose_name='教育经历')

    class Meta:
        verbose_name = '相关经历'
        verbose_name_plural = '相关经历'

    def __str__(self):
        return '相关经历'


