from django.db import models

from products.models import *


class Order(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=64)
    delivery_address = models.CharField(max_length=256, blank=True)
    entrance = models.CharField(max_length=8, blank=True)
    floor = models.CharField(max_length=4, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Заказ {self.name} {self.surname} от {self.date}"

    def total_price(self):
        total_sum = 0
        for product in self.products.all():
            total_sum += product.price() * product.quantity
        return total_sum


class OrderedProduct(models.Model):
    order = models.ForeignKey(
        to=Order, related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    product_version = models.ForeignKey(
        to=ProductVersion, related_name='ordered_products',
        on_delete=models.CASCADE)
    option_id = models.IntegerField(default=0)

    def price(self):
        return self.product_version.price

    def name(self):
        if self.option_id:
            return self.product_version.content_object.options.get(
                pk=self.option_id).__str__()
        else:
            return self.product_version.content_object.__str__()

    def product_code(self):
        if self.option_id:
            return self.product_version.content_object.options.get(
                pk=self.option_id).product_code
        else:
            return self.product_version.content_object.product_code
