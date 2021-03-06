# Generated by Django 3.1.3 on 2021-10-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('ID_Accion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Accion', models.CharField(choices=[('Edicion_Perfil', 'Edicion_Perfil'), ('Crear_Usuario', 'Crear_Usuario'), ('Activar_Usuario', 'Activar_Usuario'), ('Punto_Venta', 'Punto_Venta')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('ID_Rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(choices=[('Admin', 'Admin'), ('Vendedor', 'Vendedor'), ('Reporte', 'Reporte')], max_length=15)),
            ],
        ),
    ]
