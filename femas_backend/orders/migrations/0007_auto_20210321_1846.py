# Generated by Django 3.1.7 on 2021-03-21 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('orders', '0006_auto_20210318_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedproductoption',
            name='product_option_version',
        ),
        migrations.AddField(
            model_name='orderedproductoption',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderedproductoption',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
