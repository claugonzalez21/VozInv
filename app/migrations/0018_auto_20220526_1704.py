# Generated by Django 2.2 on 2022-05-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220526_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figura',
            name='area',
        ),
        migrations.AddField(
            model_name='figura',
            name='area',
            field=models.ManyToManyField(help_text='Seleccione un area para este persona', to='app.Area'),
        ),
    ]
