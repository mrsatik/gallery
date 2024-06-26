# Generated by Django 5.0.3 on 2024-03-09 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('photo_img', models.FileField(upload_to='images/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos list',
            },
        ),
    ]
