from django.db import models


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
        abstract = True


class ProductPhoto(models.Model):
    photo = models.ImageField(
        upload_to='product_photos',
        verbose_name='изображение'
    )

    class Meta:
        abstract = True
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товара"


class ProductVideo(models.Model):
    video = models.FileField(
        upload_to='product_videos',
        verbose_name='видео'
    )

    class Meta:
        abstract = True
        verbose_name = "видео товара"
        verbose_name_plural = "видео товара"


class Sofa(Product):
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

    class Meta:
        verbose_name = "диван"
        verbose_name_plural = "диваны"


class SofaOption(models.Model):
    sofa = models.ForeignKey(
        to=Sofa,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='диван'
    )
    size = models.CharField(
        max_length=128,
        verbose_name="размер"
    )

    def __str__(self) -> str:
        return f"Модификация {self.sofa}"


class SofaPhoto(ProductPhoto):
    sofa = models.ForeignKey(
        to=Sofa,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.sofa}'


class SofaVideo(ProductVideo):
    sofa = models.ForeignKey(
        to=Sofa,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.sofa}'


class Bed(Product):
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

    class Meta:
        verbose_name = "кровать"
        verbose_name_plural = "кровати"


class BedPhoto(ProductPhoto):
    bed = models.ForeignKey(
        to=Bed,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.bed}'


class BedVideo(ProductVideo):
    bed = models.ForeignKey(
        to=Bed,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.bed}'


class Table(Product):
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )
    collection = models.CharField(
        max_length=128,
        verbose_name='коллекция',
        blank=True
    )

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"


class TablePhoto(ProductPhoto):
    table = models.ForeignKey(
        to=Table,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.table}'


class TableVideo(ProductVideo):
    table = models.ForeignKey(
        to=Table,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.table}'


class Armchair(Product):
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    class Meta:
        verbose_name = "кресло"
        verbose_name_plural = "кресла"


class ArmchairPhoto(ProductPhoto):
    armchair = models.ForeignKey(
        to=Armchair,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.armchair}'


class ArmchairVideo(ProductVideo):
    armchair = models.ForeignKey(
        to=Armchair,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.armchair}'


class Chair(Product):
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    class Meta:
        verbose_name = "стул"
        verbose_name_plural = "стулья"


class ChairPhoto(ProductPhoto):
    chair = models.ForeignKey(
        to=Chair,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.chair}'


class ChairVideo(ProductVideo):
    chair = models.ForeignKey(
        to=Chair,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.chair}'


class Kitchenware(Product):

    class Meta:
        verbose_name = "кухонная утварь"
        verbose_name_plural = "кухонная утварь"


class KitchenwarePhoto(ProductPhoto):
    kitchenware = models.ForeignKey(
        to=Kitchenware,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.kitchenware}'


class KitchenwareVideo(ProductVideo):
    kitchenware = models.ForeignKey(
        to=Kitchenware,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.kitchenware}'


class Accessory(Product):
    type = models.CharField(
        max_length=128,
        verbose_name='тип'
    )

    class Meta:
        verbose_name = "аксесуар"
        verbose_name_plural = "аксесуары"


class AccessoryPhoto(ProductPhoto):
    accessory = models.ForeignKey(
        to=Accessory,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Фотография {self.accessory}'


class AccessoryVideo(ProductVideo):
    accessory = models.ForeignKey(
        to=Accessory,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='фотография'
    )

    def __str__(self) -> str:
        return f'Видео {self.accessory}'
