# Generated by Django 3.1.7 on 2021-03-15 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('orders', '0002_auto_20210314_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productincart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='productincart',
            name='product_content_type',
        ),
        migrations.RemoveField(
            model_name='productincart',
            name='product_option_content_type',
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product_content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_products', to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product_option_content_type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_options', to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product_option_id',
            field=models.PositiveIntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='entrance',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='floor',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='ProductInCart',
        ),
    ]
