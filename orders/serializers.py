#coding=utf-8
from .models import *
from goods.models import Good
from goods.serializers import GoodSerializer
from rest_framework import serializers

"""
{
    "amount": 2,
    "note": "bbb",
    "state": 2,
    "items":[
    {"good":105,"qty":1,"amount":10},
    {"good":106,"qty":2,"amount":20}
    ]
}
"""
class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    good = GoodSerializer(read_only=True)
    qty = serializers.IntegerField(default=1)
    price = serializers.IntegerField(default=2)

    class Meta:
        model = CartItem
        fields = ['id','good', 'price', 'qty', 'created_at', 'user']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGoodItem  
        fields = ['id', 'good', 'qty', 'amount', "good"]

class OrderGoodItemSerializer(serializers.ModelSerializer):
    good = GoodSerializer()
    class Meta:
        model = OrderGoodItem  
        fields = ['id', 'good', 'qty', 'amount', "good"]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','created_at', 'user', 'amount', 'note', 'state', 'items']
        depth = 1


    def create(self,validated_data):
        """
            重写create，实现嵌套创建OrderItem
        """
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderGoodItem.objects.create( order=order, **item_data)
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderGoodItemSerializer(many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = ['id','created_at', 'user', 'amount', 'note', 'state', 'items', 'address', 'tel']