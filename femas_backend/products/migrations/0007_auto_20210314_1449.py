# Generated by Django 3.1.7 on 2021-03-14 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0006_auto_20210314_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sofaoption',
            options={'verbose_name': 'модификация дивана', 'verbose_name_plural': 'модификации дивана'},
        ),
        migrations.AddField(
            model_name='productvideo',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvideo',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
