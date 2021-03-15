from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
        to=Order, on_delete=models.CASCADE, related_name="products"
    )
    quantity = models.PositiveSmallIntegerField(default=1)

    product_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        related_name='ordered_products'
    )
    product_id = models.PositiveIntegerField()
    product_object = GenericForeignKey(
        'product_content_type', 'product_id')

    product_option_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        related_name='ordered_options',
        blank=True)
    product_option_id = models.PositiveIntegerField(blank=True)
    product_option_object = GenericForeignKey(
        'product_option_content_type', 'product_option_id')

    def price(self):
        if (self.product_option_id and
                self.product_option_object.price):
            return self.product_option_object.price
        else:
            return self.product_object.price

    def name(self):
        if self.product_option_id:
            return self.product_option_object.__str__()
        else:
            return self.product_object.__str__()

    def product_code(self):
        if (self.product_option_id and
                self.product_option_object.product_code):
            return self.product_option_object.product_code
        else:
            return self.product_object.product_code
