# Generated by Django 3.1.7 on 2021-04-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ready_interiors', '0002_auto_20210331_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='interior',
            name='main_photo',
            field=models.ImageField(default='kek', upload_to='interior_photos', verbose_name='основное изображение'),
            preserve_default=False,
        ),
    ]
