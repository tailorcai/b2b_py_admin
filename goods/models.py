from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    parent_ids = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100, blank=True) # 商品编号(sku编号？)
    price = models.IntegerField()
    in_sale = models.BooleanField()          
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    parent_good = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)
    pic_url = models.CharField(max_length=255,null=True,blank=True)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_deleted = models.BooleanField()
   
    def __str__(self):
        return self.name

class Attribute(models.Model):
    good = models.ForeignKey(Good, related_name="props", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255,null=True,blank=True)
    blob = models.TextField(null=True,blank=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
