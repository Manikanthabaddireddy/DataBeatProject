import site
from django.contrib import admin
from product.models import Product


class Admin(admin.ModelAdmin):
    list_display=['id','product_name','quantity','price']
# Register your models here.
admin.site.register(Product,Admin)