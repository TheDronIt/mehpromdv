# Generated by Django 3.0.8 on 2021-01-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(upload_to='web/static/img/news/'),
        ),
    ]
