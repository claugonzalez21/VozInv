# Generated by Django 3.2 on 2022-06-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_remove_noticia_nombre_protagonista'),
    ]

    operations = [
        migrations.AddField(
            model_name='figura',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
