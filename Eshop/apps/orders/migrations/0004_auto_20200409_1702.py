# Generated by Django 2.2.4 on 2020-04-09 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200409_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('aee3e16d-1284-4527-85a2-af5268d6ecc3')),
        ),
    ]
