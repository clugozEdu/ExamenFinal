from django.contrib import admin
from .models import Product, Sales, Category, Marca


class ProducAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'active')
    search_fields = ('active', 'category__name')
    list_filter = ('category', 'active')
    
class SalesAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_amount', 'active', 'created_at')
    search_fields = ('product__name', 'active')
    list_filter = ('product', 'active')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active')
    search_fields = ('active', 'name')
    list_filter = ('name', 'active')
    
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active')
    search_fields = ('active', 'name')
    list_filter = ('name', 'active')
    


# Register your models here.
admin.site.register(Product, ProducAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Marca, MarcaAdmin)