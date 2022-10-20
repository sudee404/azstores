from django.contrib import admin
from store_app.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price')