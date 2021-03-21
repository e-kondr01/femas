# Generated by Django 3.1.7 on 2021-03-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='active_till',
            field=models.DateTimeField(blank=True, null=True, verbose_name='активно до'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='promo_photos', verbose_name='изображение'),
        ),
    ]
