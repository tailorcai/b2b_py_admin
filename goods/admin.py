from django.contrib import admin

# Register your models here.
from .models import Good, Category

admin.site.register(Good)
admin.site.register(Category)