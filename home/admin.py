from django.contrib import admin

# Register your models here.
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at')
    ordering = ('created_at',)
    
# class UserActivityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'product', 'action', 'timestamp')
#     search_fields = ('user_username', 'product_name', 'action')
#     list_filter = ('action', 'timestamp')
#     ordering = ('-timestamp',)
    
admin.site.register(Products, ProductsAdmin)
# admin.site.register(UserActivity, UserActivityAdmin)