# Generated by Django 5.0.6 on 2024-06-22 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappcafe', '0015_venta_cantidad_venta_producto_delete_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappcafe.producto'),
        ),
    ]
