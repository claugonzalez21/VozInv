# Generated by Django 3.2 on 2022-06-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20220609_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
