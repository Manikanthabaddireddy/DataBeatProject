from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    price=models.IntegerField()