# Generated by Django 4.1 on 2022-11-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
