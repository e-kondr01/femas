# Generated by Django 3.1.7 on 2021-04-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0005_auto_20210329_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='text',
        ),
        migrations.AddField(
            model_name='promo',
            name='main',
            field=models.BooleanField(default=False, verbose_name='основная картинка'),
        ),
    ]
