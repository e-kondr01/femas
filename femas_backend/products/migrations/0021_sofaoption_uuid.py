# Generated by Django 3.1.7 on 2021-03-29 17:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210329_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofaoption',
            name='uuid',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, null=True),
        ),
    ]
