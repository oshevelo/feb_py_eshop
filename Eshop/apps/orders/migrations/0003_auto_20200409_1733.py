# Generated by Django 2.2.4 on 2020-04-09 17:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200408_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('c098e33b-d23a-4bbc-8071-7c7a7c9019fd')),
        ),
    ]
