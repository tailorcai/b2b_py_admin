#coding=utf-8
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( "id", "username", "date_joined" ,)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields =( "user", "gender", "nickname", "telephone","birthday","email","realname", "avatar")

class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserAddress
        fields = '__all__'

    def cleanup(self, address):
        # remove old default
        for ua in UserAddress.objects.filter(user=address.user).exclude(pk=address.id).filter(is_default=True).all():
            ua.is_default=False
            ua.save()
        
    def create(self, validated_data):
        address = super(UserAddressSerializer,self).create(validated_data=validated_data)
        if address.is_default:
            self.cleanup(address)
        return address

    def update(self,instance, validated_data):
        address = super(UserAddressSerializer,self).update(instance, validated_data=validated_data)
        if address.is_default:
            self.cleanup(address)
        return address
