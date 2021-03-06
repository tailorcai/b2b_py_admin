# Generated by Django 2.1.4 on 2018-12-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='realname',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='性别'),
        ),
    ]
