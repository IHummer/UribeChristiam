# Generated by Django 3.0 on 2019-12-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0005_imagenmascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenmascota',
            name='mascota_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]