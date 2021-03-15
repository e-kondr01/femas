from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ProductPhoto(models.Model):

    photo = models.ImageField(
        upload_to="product_photos", verbose_name="изображение")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        return f"{self.content_object}"

    class Meta:
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товара"


class ProductVideo(models.Model):
    video = models.FileField(upload_to="product_videos", verbose_name="видео")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        return f"{self.content_object}"

    class Meta:
        verbose_name = "видео товара"
        verbose_name_plural = "видео товара"


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="наименование")
    description = models.TextField(blank=True, verbose_name="описание")
    photos = GenericRelation(ProductPhoto)
    videos = GenericRelation(ProductVideo)
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                blank=True, verbose_name="стоимость")
    product_code = models.CharField(max_length=32,
                                    verbose_name="артикул",
                                    blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        abstract = True


class Sofa(Product):
    mechanism = models.CharField(max_length=128, verbose_name="механизм")
    collection = models.CharField(
        max_length=128, verbose_name="коллекция", blank=True)

    class Meta:
        verbose_name = "диван"
        verbose_name_plural = "диваны"


class SofaOption(models.Model):
    sofa = models.ForeignKey(
        to=Sofa, on_delete=models.CASCADE, related_name="options",
        verbose_name="диван"
    )
    size = models.CharField(max_length=128, verbose_name="размер")
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                verbose_name="стоимость")
    product_code = models.CharField(max_length=128, verbose_name="артикул",
                                    blank=True)

    def __str__(self) -> str:
        return f"{self.sofa} {self.size}"

    class Meta:
        verbose_name = "модификация дивана"
        verbose_name_plural = "модификации дивана"


class Bed(Product):
    size = models.CharField(max_length=128, verbose_name="размер")
    mechanism = models.CharField(max_length=128, verbose_name="механизм")
    headboard = models.CharField(
        max_length=128, verbose_name="форма изголовья")

    class Meta:
        verbose_name = "кровать"
        verbose_name_plural = "кровати"


class Table(Product):
    type = models.CharField(max_length=128, verbose_name="тип")
    collection = models.CharField(
        max_length=128, verbose_name="коллекция", blank=True)

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"


class Armchair(Product):
    type = models.CharField(max_length=128, verbose_name="тип")

    class Meta:
        verbose_name = "кресло"
        verbose_name_plural = "кресла"


class Chair(Product):
    type = models.CharField(max_length=128, verbose_name="тип")

    class Meta:
        verbose_name = "стул"
        verbose_name_plural = "стулья"


class Kitchenware(Product):
    class Meta:
        verbose_name = "кухонная утварь"
        verbose_name_plural = "кухонная утварь"


class Accessory(Product):
    type = models.CharField(max_length=128, verbose_name="тип")

    class Meta:
        verbose_name = "аксесуар"
        verbose_name_plural = "аксесуары"
