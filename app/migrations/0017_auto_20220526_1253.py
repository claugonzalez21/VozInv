# Generated by Django 2.2 on 2022-05-26 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20220526_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='area',
        ),
        migrations.AlterField(
            model_name='figura',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Area'),
        ),
    ]
