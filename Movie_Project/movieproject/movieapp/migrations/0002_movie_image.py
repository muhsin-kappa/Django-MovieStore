# Generated by Django 4.1.5 on 2023-01-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='demo', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
