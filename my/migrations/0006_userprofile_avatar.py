# Generated by Django 2.1.4 on 2018-12-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0005_useraddress_area_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=10, verbose_name='头像'),
        ),
    ]