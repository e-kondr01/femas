# Generated by Django 3.1.7 on 2021-03-13 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210311_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='armchair',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='chair',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='kitchenware',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='sofa',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
        migrations.AlterField(
            model_name='table',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='общие данные товара'),
        ),
    ]
