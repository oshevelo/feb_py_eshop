# Generated by Django 2.2.12 on 2020-05-06 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0008_auto_20200502_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='shipment_status_date',
            new_name='shipment_status_date_updated',
        ),
        migrations.AddField(
            model_name='shipment',
            name='shipment_address_region',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='shipment_status_date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_address_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_adress_apartment',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_adress_street',
            field=models.CharField(max_length=50),
        ),
    ]
