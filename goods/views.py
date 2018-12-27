from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Good, Category


class GoodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Good.objects.all().order_by('-create_time')
    #serializer_class = GoodSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('id', 'name')
    filter_fields = ('category_id',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodDetailSerializer
        else:
            return GoodSerializer

class RecommendView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        top_c = [{ 'id':c.id, 'name':c.name } for c in Category.objects.filter( parent_id=1 )]
        for c in top_c:
            c['children'] = [{'id': d.id, 'name': d.name} for d in Category.objects.filter( parent_id=c['id'] )]
        return Response({ 'category': top_c })

class CategorySubGoodsView(APIView):
    def get(self,request,format=None):
        queryset = Good.objects.filter(category__parent_ids__contains='/'+request.query_params.get('category_id', 1)+'/')
        return Response( GoodSerializer(queryset, many=True).data )