from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from goods.models import Good
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    def get_queryset(self):
        # Ordering?
        return CartItem.objects.filter(user=self.request.user)

    def create(self,request, *args, **kwargs):
        """
            提供good id即可，加入购物车
        """
        good = get_object_or_404( Good.objects.all(), id=request.data['good'])
        
        if self.get_queryset().filter( good=good ).count()>0:
            raise Exception('Good is in cart already')
        
        cartItem = CartItem.objects.create(good=good,price=good.price,qty=1, user=self.request.user)
        cartItem.save()

        headers = self.get_success_headers(cartItem)
        return Response( CartItemSerializer(cartItem).data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self,request, *args, **kwargs):
        """
            提供good id 即可删除
        """
        ids = request.data['id']
        for id in ids:
            self.get_queryset().filter(pk=id).delete()
        
        return Response( True, status=status.HTTP_204_NO_CONTENT, headers=self.get_success_headers(request.data) )

class OrderViewSet(viewsets.ModelViewSet):
    #serializer_class = OrderSerializer
    def get_queryset(self):
        # Ordering?
        return Order.objects.filter(user=self.request.user)

    # def alist(self,request, *args, **kwargs):
    #     query_set = self.get_queryset()
    #     serializer = OrderDetailSerializer(query_set, many=True)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderSerializer
        elif self.action == 'list':
            return OrderDetailSerializer

class OrderCountView(APIView):
    def get(self,request, format=None):
        """
            订单按照状态统计数量
        """
        orderS = Order.objects.filter(user=self.request.user).values_list('state').annotate(Count('id'))
        ret = {}
        for o in orderS:
            ret[o[0]] = o[1]
        return Response(ret)

class PlaceOrderView(APIView):
    def post(self,request,format=None):
        """
            实现一个最简单的，将购物车转换为订单的逻辑
        """
        ids = request.data['orderId']
        if len(ids) <=0:
            raise Exception("invalid orderId ")
        items = CartItem.objects.filter( pk__in = ids)
        if len(ids) != len(items):
            raise Exception("购物车数据异常，请重新发起订单，TODO")
        
        amount = 0
        for item in items:
            amount += item.price * item.qty

        order = Order.objects.create(
            address=request.data['address'],
            tel=request.data['tel'], 
            amount=amount,
            note=request.data['note'],
            state=0,
            user=request.user
        )
        
        order_items = [order.items.create(good=item.good,qty=item.qty,amount=item.price*item.qty) for item in items]
        order.save()

        # 清除购物车
        items.delete()

        return Response( OrderSerializer(order).data )