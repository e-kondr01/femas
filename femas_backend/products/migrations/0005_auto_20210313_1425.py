# Generated by Django 3.1.7 on 2021-03-13 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210313_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sofa',
            name='size',
        ),
        migrations.CreateModel(
            name='SofaOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=128, verbose_name='размер')),
                ('sofa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='products.sofa', verbose_name='диван')),
            ],
        ),
    ]
