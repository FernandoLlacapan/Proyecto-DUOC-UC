# Generated by Django 5.0.6 on 2024-06-22 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappcafe', '0016_alter_venta_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
    ]