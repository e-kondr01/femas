# Generated by Django 3.1.7 on 2021-03-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210321_1846'),
        ('products', '0016_auto_20210321_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sofaoption',
            old_name='sofa',
            new_name='product',
        ),
        migrations.DeleteModel(
            name='ProductOptionVersion',
        ),
    ]
