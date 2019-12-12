# Generated by Django 3.0 on 2019-12-11 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_detallemascota_detallemedicina_detallevacuna_medicina_registroclinico_vacuna'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenMascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota_img', models.ImageField(upload_to='images/')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.Mascota')),
            ],
        ),
    ]