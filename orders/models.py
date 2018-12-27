from django.db import models
from django.contrib.auth.models import User
from goods.models import Good

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO: make snapshot for the good in case good changed, including price ..
    # maybe MVCC for the good object is a must ???


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    note = models.TextField()
    address = models.CharField(max_length=256)
    tel = models.CharField('电话', max_length=50, blank=True)
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class OrderGoodItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    good = models.ForeignKey(Good, null=True, on_delete=models.SET_NULL)           # todo: 改为统一的good 快照对象，节省空间
    qty = models.IntegerField()
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

#class OrderCouponItem(models.Model):
    