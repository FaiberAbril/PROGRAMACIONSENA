# Generated by Django 4.1.13 on 2024-03-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_remove_client_dni_client_cedula_client_municipality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='codigoReferencia',
            field=models.CharField(default=1, max_length=25, unique=True, verbose_name='codigoReferencia'),
        ),
    ]
