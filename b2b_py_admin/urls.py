#coding=utf-8
"""b2b_py_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from goods.views import GoodsViewSet, RecommendView, CategorySubGoodsView
from orders.views import CartItemViewSet,OrderViewSet,PlaceOrderView,OrderCountView
from my.views import ProfileViewSet,UserAddressViewSet
from django.conf.urls import url, include
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('goods', GoodsViewSet)
router.register('cart/items', CartItemViewSet, basename="cartitem")
router.register('orders', OrderViewSet, basename="order")
router.register('profile', ProfileViewSet, basename="profile")
router.register('address', UserAddressViewSet, basename="address")

urlpatterns = [
    url('api/orderNum/', OrderCountView.as_view()),
    url('api/placeorder/', PlaceOrderView.as_view()),
    url('api/recommend/', RecommendView.as_view()),
    url('api/classifications/', CategorySubGoodsView.as_view()),
   url('api/', include(router.urls)),
    path('admin/', admin.site.urls),
   url('^api-goods/', include('rest_framework.urls', namespace='rest_framework')),
   # 提供认证服务
   url('^api-token-auth/', views.obtain_auth_token)    
]
