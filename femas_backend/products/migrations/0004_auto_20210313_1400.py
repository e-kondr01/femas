# Generated by Django 3.1.7 on 2021-03-13 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210313_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessoryVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArmchairPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArmchairVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BedPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChairPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChairVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KitchenwarePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KitchenwareVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SofaPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SofaVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TablePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'изображение товара',
                'verbose_name_plural': 'изображения товара',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='product_videos', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'видео товара',
                'verbose_name_plural': 'видео товара',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='productphoto',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvideo',
            name='product',
        ),
        migrations.RemoveField(
            model_name='accessory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='armchair',
            name='product',
        ),
        migrations.RemoveField(
            model_name='bed',
            name='product',
        ),
        migrations.RemoveField(
            model_name='chair',
            name='product',
        ),
        migrations.RemoveField(
            model_name='kitchenware',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sofa',
            name='product',
        ),
        migrations.RemoveField(
            model_name='table',
            name='product',
        ),
        migrations.AddField(
            model_name='accessory',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='name',
            field=models.CharField(default='asd', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='armchair',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='armchair',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bed',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='bed',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chair',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='chair',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitchenware',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='kitchenware',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sofa',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='sofa',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='table',
            name='name',
            field=models.CharField(default='a', max_length=256, verbose_name='наименование'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductPhoto',
        ),
        migrations.DeleteModel(
            name='ProductVideo',
        ),
        migrations.AddField(
            model_name='tablevideo',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.table', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='tablephoto',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.table', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='sofavideo',
            name='sofa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.sofa', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='sofaphoto',
            name='sofa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.sofa', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='kitchenwarevideo',
            name='kitchenware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.kitchenware', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='kitchenwarephoto',
            name='kitchenware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.kitchenware', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='chairvideo',
            name='chair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.chair', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='chairphoto',
            name='chair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.chair', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='bedvideo',
            name='bed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.bed', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='bedphoto',
            name='bed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.bed', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='armchairvideo',
            name='armchair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.armchair', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='armchairphoto',
            name='armchair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.armchair', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='accessoryvideo',
            name='accessory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.accessory', verbose_name='фотография'),
        ),
        migrations.AddField(
            model_name='accessoryphoto',
            name='accessory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.accessory', verbose_name='фотография'),
        ),
    ]
