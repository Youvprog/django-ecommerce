from django.contrib import admin
from .models import Product, Category, Orderitems, Cart, VilleShipping, Filter, Color
# Register your models here.


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','quantity','ordered','ordered_date']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','ordered','ordered_date']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock']


class VilleAdmin(admin.ModelAdmin):
    list_display = ['name','price_shipping']

class FilterAdmin(admin.ModelAdmin):
    list_display = ['name']

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Orderitems, OrderItemsAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(VilleShipping, VilleAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Color, ColorAdmin)
