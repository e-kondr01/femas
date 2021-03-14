from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from products.models import *


class Cart(models.Model):
    pass


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        related_name='products'
    )
    quantity = models.SmallIntegerField(
        verbose_name='количество'
    )

    product_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        related_name='products_in_cart'
    )
    product_id = models.PositiveIntegerField()
    product_content_object = GenericForeignKey(
        'product_content_type', 'product_id')

    product_option_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        related_name='product_options_in_cart')
    product_option_id = models.PositiveIntegerField()
    product_option_content_object = GenericForeignKey(
        'product_option_content_type', 'product_option_id')


class Order(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=128)
    delivery_address = models.CharField(max_length=256)
    entrance = models.CharField(max_length=8)
    floor = models.CharField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Заказ {self.name} {self.surname} от {self.date}'


class OrderedProduct(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='products'
    )
