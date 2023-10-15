from django.contrib import admin
from .models import Profile, Products, Category, SubCategory

# Register your models here.
admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(SubCategory)