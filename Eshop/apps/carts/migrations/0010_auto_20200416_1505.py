# Generated by Django 2.2.12 on 2020-04-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_delete_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_in',
            new_name='product',
        ),
    ]
