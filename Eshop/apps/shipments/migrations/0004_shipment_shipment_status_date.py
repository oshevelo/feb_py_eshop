# Generated by Django 2.2.12 on 2020-05-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0003_shipment_shipment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='shipment_status_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]