from django.contrib import admin

from .models import *


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price',)


class OrderedProductAdmin(admin.ModelAdmin):
    readonly_fields = ('price', 'name', 'product_code')


class OrderedProductOptionAdmin(admin.ModelAdmin):
    readonly_fields = ('price', 'name', 'product_code')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedProduct, OrderedProductAdmin)
admin.site.register(OrderedProductOption, OrderedProductOptionAdmin)
