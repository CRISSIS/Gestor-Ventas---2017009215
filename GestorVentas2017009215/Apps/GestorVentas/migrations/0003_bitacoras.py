# Generated by Django 3.1.3 on 2021-10-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestorVentas', '0002_acciones_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacoras',
            fields=[
                ('ID_Bitacora', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=50)),
                ('hora', models.CharField(max_length=50)),
                ('direccion_IP', models.CharField(max_length=50)),
            ],
        ),
    ]