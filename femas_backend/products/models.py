import uuid

from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


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


class ProductVersion(models.Model):
    current = models.BooleanField(default=False)
    actual_from = models.DateTimeField(auto_now_add=True)
    actual_to = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        s = (f'{self.content_object} по цене {self.price} от '
             f'{self.actual_from} до {self.actual_to}')
        return s


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="наименование")
    description = models.TextField(blank=True, verbose_name="описание")
    photos = GenericRelation(ProductPhoto)
    videos = GenericRelation(ProductVideo)
    versions = GenericRelation(ProductVersion)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="стоимость")
    product_code = models.CharField(max_length=32,
                                    verbose_name="артикул",
                                    blank=True)
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self) -> str:
        return f"{self.name}"

    def has_options(self):
        if self.options.count():
            return True
        else:
            return False

    def class_name(self):
        return self.__class__.__name__

    def get_absolute_url(self):
        return f'https://femas.ru/{self.class_name()}s/{self.uuid}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        previous_version = self.versions.filter(current=True).first()
        if previous_version and previous_version.price != self.price:
            version = ProductVersion.objects.create(
                content_object=self, price=self.price, current=True)
            version.save()
            previous_version.current = False
            previous_version.actual_to = timezone.now()
            previous_version.save()
        if not previous_version:
            version = ProductVersion.objects.create(
                content_object=self, price=self.price, current=True)
            version.save()

    class Meta:
        abstract = True


class ProductOption(models.Model):
    product_code = models.CharField(max_length=128, verbose_name="артикул")
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)

    class Meta:
        abstract = True

    def class_name(self):
        return self.__class__.__name__


class Sofa(Product):
    mechanism = models.CharField(max_length=128, verbose_name="механизм")
    collection = models.CharField(
        max_length=128, verbose_name="коллекция", blank=True)

    class Meta:
        verbose_name = "диван"
        verbose_name_plural = "диваны"


class SofaOption(ProductOption):
    product = models.ForeignKey(
        to=Sofa, on_delete=models.CASCADE, related_name="options",
        verbose_name="диван"
    )
    size = models.CharField(max_length=128, verbose_name="размер")

    def __str__(self) -> str:
        return f"{self.product} {self.size}"

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
