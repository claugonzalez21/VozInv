# Generated by Django 3.2 on 2022-06-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_figura_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='figura',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='figura',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='figura',
            name='imagen3',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
