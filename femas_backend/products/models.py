from django.db import models


"""
class (models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
"""


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="наименование"
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание'
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "товар, общие данные"
        verbose_name_plural = "товары, общие данные"


class Sofa(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    size = models.CharField(
        max_length=128,
        verbose_name="размер"
    )
    mechanism = models.CharField(
        max_length=128,
        verbose_name='механизм'
    )
    collection = models.CharField(
        max_length=128,
        verbose_name='коллекция',
        blank=True
    )
    code = models.CharField(
        max_length=128,
        verbose_name="артикул"
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "диван"
        verbose_name_plural = "диваны"


class Bed(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    size = models.CharField(
        max_length=128,
        verbose_name="размер"
    )
    mechanism = models.CharField(
        max_length=128,
        verbose_name='механизм'
    )
    headboard = models.CharField(
        max_length=128,
        verbose_name='форма изголовья'
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "кровать"
        verbose_name_plural = "кровати"


class Table(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )
    collection = models.CharField(
        max_length=128,
        verbose_name='коллекция',
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"


class Armchair(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "кресло"
        verbose_name_plural = "кресла"


class Chair(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "стул"
        verbose_name_plural = "стулья"


class Kitchenware(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "кухонная утварь"
        verbose_name_plural = "кухонная утварь"


class Accessory(models.Model):
    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='общие данные товара')
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "аксесуар"
        verbose_name_plural = "аксесуары"


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
