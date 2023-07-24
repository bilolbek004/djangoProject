from django.contrib import admin
from django.contrib.admin import ModelAdmin

# from apps.models import Product, Category, Rate
from models import Product, Category, Rate


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    filter_horizontal = ['categories']


# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Rate)
