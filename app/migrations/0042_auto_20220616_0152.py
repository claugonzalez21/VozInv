# Generated by Django 3.2 on 2022-06-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_curiosidad_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='titulo',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='resumen',
            field=models.TextField(default=None, max_length=10000, null=True),
        ),
    ]
