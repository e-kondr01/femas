import uuid

from django.db import models


class Interior(models.Model):
    COLOR_CHOICES = (
        ('красный', 'красный'),
        ('зелёный', 'зелёный'),
        ('синий', 'синий'),
        ('оранжевый', 'оранжевый'),
    )
    SQUARE_CHOICES = (
        ('до 30м2', 'до 30м2'),
        ('до 50м2', 'до 50м2'),
    )
    ROOM_TYPE_CHOICES = (
        ('детская', 'детская'),
        ('кухня', 'кухня'),
    )

    name = models.CharField(max_length=512, verbose_name="наименование")
    color = models.CharField(
        max_length=64, verbose_name='цвет', choices=COLOR_CHOICES)
    square = models.CharField(
        max_length=64, verbose_name='площадь', choices=SQUARE_CHOICES)
    room_type = models.CharField(
        max_length=64, verbose_name='тип комнаты', choices=ROOM_TYPE_CHOICES)
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "готовый интерьер"
        verbose_name_plural = "готовые интерьеры"


class InteriorPhoto(models.Model):

    photo = models.ImageField(
        upload_to="interior_photos", verbose_name="изображение")
    interior = models.ForeignKey(
        to=Interior,
        on_delete=models.CASCADE,
        verbose_name='интерьер',
        related_name='photos'
    )

    def __str__(self) -> str:
        return f"фото {self.interior}"

    class Meta:
        verbose_name = "изображение интерьера"
        verbose_name_plural = "изображения интерьера"
