# Generated by Django 3.1.7 on 2021-03-29 17:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20210329_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sofaoption',
            name='uuid',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True),
        ),
    ]