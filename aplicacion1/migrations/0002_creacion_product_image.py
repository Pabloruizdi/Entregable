# Generated by Django 4.1.4 on 2023-02-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creacion',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
    ]