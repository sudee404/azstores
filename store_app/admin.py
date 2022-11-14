from django.contrib import admin
from store_app.models import Product,Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'gender', 'price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)