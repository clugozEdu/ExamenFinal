from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Create your models here.
class Marca(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
      

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name
    
    @property
    def total_amount(self):
        return self.product.price * self.quantity
      
      
@receiver(post_save, sender=Sales)
def update_product_stock(sender, instance, created, **kwargs):
  if created:
    product = instance.product
    product.quantity -= instance.quantity
    product.save()
    
    
@receiver(pre_delete, sender=Sales)
def update_product_stock_on_delete(sender, instance, **kwargs):
  product = instance.product
  product.quantity += instance.quantity
  product.save()
  # desactive
  instance.active = False
