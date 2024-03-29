# Generated by Django 3.1.7 on 2021-03-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0010_auto_20210315_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=False)),
                ('actual_from', models.DateTimeField(auto_now_add=True)),
                ('actual_to', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_id', models.PositiveIntegerField()),
                ('product_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOptionVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=False)),
                ('actual_from', models.DateTimeField(auto_now_add=True)),
                ('actual_to', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_option_id', models.PositiveIntegerField(blank=True)),
                ('product_option_content_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
