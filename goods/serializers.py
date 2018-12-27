#coding=utf-8
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
from django.utils import six

class PublicAttributeListSerializer(serializers.ListSerializer):
    """
        Hack!!!
    """
    def to_representation(self,data):
        data = data.filter(level__gte=0) #.all() if isinstance(data, models.Manager) else data
        return super(PublicAttributeListSerializer,self).to_representation(data)

class AttributeSerializer(serializers.ModelSerializer):
    real_value = serializers.SerializerMethodField()
    class Meta:
        model = Attribute
        fields = ['name', 'real_value', 'level']
        list_serializer_class=PublicAttributeListSerializer #Hack!!!

    def get_real_value(self, obj):
        if obj.value is None:
            return obj.blob
        return obj.value

class GoodSerializer(serializers.ModelSerializer):
    present_price = serializers.IntegerField(source='price')
    orl_price = serializers.IntegerField(source='price',read_only=True)
    amount = serializers.IntegerField(default=10)

    class Meta:
        model = Good
        fields = ['id','name','shop_id', 'present_price', 'orl_price', 'in_sale', 'amount', 'pic_url']

class GoodDetailSerializer(serializers.ModelSerializer):
    present_price = serializers.IntegerField(source='price')
    orl_price = serializers.IntegerField(source='price',read_only=True)
    amount = serializers.IntegerField(default=10)
    props = AttributeSerializer(many=True)  # public attributes
    #pictures

    class Meta:
        model = Good
        fields = ['id','name','shop_id', 'present_price', 'orl_price', 'in_sale', 'amount', 'pic_url', 'description', 'props' ]        
