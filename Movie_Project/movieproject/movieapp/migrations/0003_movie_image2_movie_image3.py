# Generated by Django 4.1.5 on 2023-01-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image2',
            field=models.ImageField(default='image', upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='image3',
            field=models.ImageField(default='image2', upload_to='gallery'),
            preserve_default=False,
        ),
    ]