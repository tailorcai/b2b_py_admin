
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    
class UserAddressViewSet(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('is_default',)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

  