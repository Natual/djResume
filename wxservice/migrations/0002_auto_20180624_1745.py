# Generated by Django 2.0.5 on 2018-06-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='payId',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='费用ID'),
        ),
        migrations.AlterField(
            model_name='fee',
            name='payMethod',
            field=models.IntegerField(verbose_name='缴纳方式：1=按月缴纳，3=按季度缴纳，12=按年缴纳'),
        ),
        migrations.AlterField(
            model_name='fee',
            name='status',
            field=models.IntegerField(verbose_name='当期缴纳状态: 0= 未缴纳完毕，1= 已缴纳完毕'),
        ),
        migrations.AlterField(
            model_name='pay_user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='用户ID'),
        ),
    ]