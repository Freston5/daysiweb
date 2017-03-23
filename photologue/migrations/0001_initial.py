# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 17:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import photologue.models
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0003_set_site_domain_and_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='title')),
                ('slug', models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', max_length=250, unique=True, verbose_name='title slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_public', models.BooleanField(default=True, help_text='Public galleries will be displayed in the default views.', verbose_name='is public')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
                'ordering': ['-date_added'],
                'get_latest_by': 'date_added',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=photologue.models.get_storage_path, verbose_name='image')),
                ('date_taken', models.DateTimeField(blank=True, help_text='Date image was taken; is obtained from the image EXIF data.', null=True, verbose_name='date taken')),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('crop_from', models.CharField(blank=True, choices=[('top', 'Top'), ('right', 'Right'), ('bottom', 'Bottom'), ('left', 'Left'), ('center', 'Center (Default)')], default='center', max_length=10, verbose_name='crop from')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='title')),
                ('slug', models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', max_length=250, unique=True, verbose_name='slug')),
                ('caption', models.TextField(blank=True, verbose_name='caption')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
                ('is_public', models.BooleanField(default=True, help_text='Public photographs will be displayed in the default views.', verbose_name='is public')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ['-date_added'],
                'get_latest_by': 'date_added',
            },
        ),
        migrations.CreateModel(
            name='PhotoEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('transpose_method', models.CharField(blank=True, choices=[('FLIP_LEFT_RIGHT', 'Flip left to right'), ('FLIP_TOP_BOTTOM', 'Flip top to bottom'), ('ROTATE_90', 'Rotate 90 degrees counter-clockwise'), ('ROTATE_270', 'Rotate 90 degrees clockwise'), ('ROTATE_180', 'Rotate 180 degrees')], max_length=15, verbose_name='rotate or flip')),
                ('color', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a black and white image, a factor of 1.0 gives the original image.', verbose_name='color')),
                ('brightness', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a black image, a factor of 1.0 gives the original image.', verbose_name='brightness')),
                ('contrast', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a solid grey image, a factor of 1.0 gives the original image.', verbose_name='contrast')),
                ('sharpness', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a blurred image, a factor of 1.0 gives the original image.', verbose_name='sharpness')),
                ('filters', models.CharField(blank=True, help_text='Chain multiple filters using the following pattern "FILTER_ONE->FILTER_TWO->FILTER_THREE". Image filters will be applied in order. The following filters are available: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE.', max_length=200, verbose_name='filters')),
                ('reflection_size', models.FloatField(default=0, help_text='The height of the reflection as a percentage of the orignal image. A factor of 0.0 adds no reflection, a factor of 1.0 adds a reflection equal to the height of the orignal image.', verbose_name='size')),
                ('reflection_strength', models.FloatField(default=0.6, help_text='The initial opacity of the reflection gradient.', verbose_name='strength')),
                ('background_color', models.CharField(default='#FFFFFF', help_text='The background color of the reflection gradient. Set this to match the background color of your page.', max_length=7, verbose_name='color')),
            ],
            options={
                'verbose_name': 'photo effect',
                'verbose_name_plural': 'photo effects',
            },
        ),
        migrations.CreateModel(
            name='PhotoSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Photo size name should contain only letters, numbers and underscores. Examples: "thumbnail", "display", "small", "main_page_widget".', max_length=40, unique=True, validators=[django.core.validators.RegexValidator(message='Use only plain lowercase letters (ASCII), numbers and underscores.', regex='^[a-z0-9_]+$')], verbose_name='name')),
                ('width', models.PositiveIntegerField(default=0, help_text='If width is set to "0" the image will be scaled to the supplied height.', verbose_name='width')),
                ('height', models.PositiveIntegerField(default=0, help_text='If height is set to "0" the image will be scaled to the supplied width', verbose_name='height')),
                ('quality', models.PositiveIntegerField(choices=[(30, 'Very Low'), (40, 'Low'), (50, 'Medium-Low'), (60, 'Medium'), (70, 'Medium-High'), (80, 'High'), (90, 'Very High')], default=70, help_text='JPEG image quality.', verbose_name='quality')),
                ('upscale', models.BooleanField(default=False, help_text='If selected the image will be scaled up if necessary to fit the supplied dimensions. Cropped sizes will be upscaled regardless of this setting.', verbose_name='upscale images?')),
                ('crop', models.BooleanField(default=False, help_text='If selected the image will be scaled and cropped to fit the supplied dimensions.', verbose_name='crop to fit?')),
                ('pre_cache', models.BooleanField(default=False, help_text='If selected this photo size will be pre-cached as photos are added.', verbose_name='pre-cache?')),
                ('increment_count', models.BooleanField(default=False, help_text='If selected the image\'s "view_count" will be incremented when this photo size is displayed.', verbose_name='increment view count?')),
                ('effect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_sizes', to='photologue.PhotoEffect', verbose_name='photo effect')),
            ],
            options={
                'verbose_name': 'photo size',
                'verbose_name_plural': 'photo sizes',
                'ordering': ['width', 'height'],
            },
        ),
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='photologue/watermarks', verbose_name='image')),
                ('style', models.CharField(choices=[('tile', 'Tile'), ('scale', 'Scale')], default='scale', max_length=5, verbose_name='style')),
                ('opacity', models.FloatField(default=1, help_text='The opacity of the overlay.', verbose_name='opacity')),
            ],
            options={
                'verbose_name': 'watermark',
                'verbose_name_plural': 'watermarks',
            },
        ),
        migrations.AddField(
            model_name='photosize',
            name='watermark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_sizes', to='photologue.Watermark', verbose_name='watermark image'),
        ),
        migrations.AddField(
            model_name='photo',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_related', to='photologue.PhotoEffect', verbose_name='effect'),
        ),
        migrations.AddField(
            model_name='photo',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.Site', verbose_name='sites'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='galleries', to='photologue.Photo', verbose_name='photos'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.Site', verbose_name='sites'),
        ),
    ]
