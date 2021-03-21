from django.db import models


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

    def __str__(self) -> str:
        return f"{self.title} от {self.created_at}"

    class Meta:
        verbose_name = "акция"
        verbose_name_plural = "акции"
