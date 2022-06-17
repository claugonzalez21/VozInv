# Generated by Django 3.2 on 2022-05-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20220528_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Ingrese una breve descripción del articulo', max_length=1000)),
            ],
        ),
    ]