# Generated by Django 3.0.7 on 2021-03-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionClientes', '0005_auto_20210303_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
