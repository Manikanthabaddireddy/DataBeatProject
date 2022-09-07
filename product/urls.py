from django.urls import path
from .views import product,Product_Report,Update

urlpatterns = [
path('product_details/',Product_Report),
path('product_details/product_form/',product),
path('product_details/product_update/<int:id>',Update),
]