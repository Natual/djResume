# Generated by Django 2.0.5 on 2018-06-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20180606_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='projectExprience',
            field=models.TextField(blank=True, verbose_name='项目经验'),
        ),
    ]