# Generated by Django 4.1.4 on 2023-02-07 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pagoo',
        ),
        migrations.RemoveField(
            model_name='ordeness',
            name='payment_method',
        ),
    ]