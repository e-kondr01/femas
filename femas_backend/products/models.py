from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=512,
        verbose_name="наименование"
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание'
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class ProductPhoto(models.Model):
    photo = models.ImageField(
        upload_to='product_photos',
        verbose_name='изображение'
        )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='товар',
        related_name='photos'
    )
    # Удалять фото при удалении товара

    def __str__(self) -> str:
        return f'изображение {self.product}'

    class Meta:
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товара"


class ProductVideo(models.Model):
    video = models.FileField(
        upload_to='product_videos',
        verbose_name='видео'
        )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='товар',
        related_name='videos'
    )
    # Удалять видео при удалении товара

    def __str__(self) -> str:
        return f'видео {self.product}'

    class Meta:
        verbose_name = "видео товара"
        verbose_name_plural = "видео товара"


class ProductOption(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='товар',
        related_name='options'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='наименование'
    )

    def __str__(self) -> str:
        return f'{self.name} {self.product}'

    class Meta:
        verbose_name = "опция товара"
        verbose_name_plural = "опции товара"


class ProductOptionChoice(models.Model):
    option = models.ForeignKey(
        to=ProductOption,
        on_delete=models.CASCADE,
        verbose_name='опция товара',
        related_name='choices'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='наименование'
    )

    def __str__(self) -> str:
        return f'{self.name} {self.option}'

    class Meta:
        verbose_name = "выбор опции товара"
        verbose_name_plural = "выборы опций товара"
