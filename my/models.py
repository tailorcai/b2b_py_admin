#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField('昵称', max_length=128, blank=True)
    telephone = models.CharField('电话', max_length=50, blank=True)
    gender = models.CharField('性别', max_length=10, blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)
    birthday = models.DateField('生日', null=True, blank=True)
    realname = models.CharField('姓名', null=True, max_length=128, blank=True)
    email = models.EmailField('邮箱', null=True, blank=True)
    avatar = models.CharField('头像', max_length=10, blank=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return "{}'s profile".format(self.user.__str__())

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    name =  models.CharField('姓名', null=True, max_length=128, blank=True)
    address = models.CharField('详细地址', null=True, max_length=256, blank=True)
    is_default = models.BooleanField('默认地址')
    province = models.CharField('省', null=True, max_length=128, blank=True)
    city = models.CharField('市', null=True, max_length=128, blank=True)
    county = models.CharField('区/县', null=True, max_length=128, blank=True)
    tel = models.CharField('电话', max_length=50, blank=True)
    area_code = models.CharField('areaCode', max_length=50, null=True,blank=True)

    