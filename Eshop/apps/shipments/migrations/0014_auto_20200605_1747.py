# Generated by Django 2.2.4 on 2020-06-05 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0013_auto_20200604_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.Order'),
        ),
    ]
