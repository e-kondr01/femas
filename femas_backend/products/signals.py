from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import ProductVersion


allowed_objects = [
    "Sofa",
    "Bed",
    "Table",
    "Armchair",
    "Chair",
    "Kitchenware",
    "Accessory",
]


@receiver(post_save)
def create_product_version(sender, instance, **kwargs):
    if sender.__name__ in allowed_objects:
        previous_version = instance.versions.filter(current=True).first()
        print(previous_version)
        if previous_version and previous_version.price != instance.price:
            version = ProductVersion.objects.create(
                content_object=instance, price=instance.price, current=True)
            version.save()
            previous_version.current = False
            previous_version.actual_to = timezone.now()
            previous_version.save()
        if not previous_version:
            version = ProductVersion.objects.create(
                content_object=instance, price=instance.price, current=True)
            version.save()
