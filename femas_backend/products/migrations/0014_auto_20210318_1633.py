# Generated by Django 3.1.7 on 2021-03-18 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210318_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productoptionversion',
            old_name='product_option_content_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='productoptionversion',
            old_name='product_option_id',
            new_name='object_id',
        ),
        migrations.RenameField(
            model_name='productversion',
            old_name='product_content_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='productversion',
            old_name='product_id',
            new_name='object_id',
        ),
    ]
