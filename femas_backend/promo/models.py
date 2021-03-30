import uuid

from django.db import models
from django.utils import timezone


tz = timezone.get_default_timezone()


class Promo(models.Model):
    title = models.CharField(max_length=512, verbose_name='заголовок')
    text = models.TextField(verbose_name="содержание")
    photo = models.ImageField(
        upload_to="promo_photos", verbose_name="изображение", blank=True)
    active = models.BooleanField(verbose_name='действует')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='активно с')
    active_till = models.DateTimeField(
        verbose_name='активно до', blank=True, null=True)
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self) -> str:
        return (f"{self.title} от "
                f"{self.created_at.astimezone(tz).strftime('%d.%m.%Y %H:%M')}")

    class Meta:
        verbose_name = "акция"
        verbose_name_plural = "акции"
