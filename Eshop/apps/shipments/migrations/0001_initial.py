# Generated by Django 2.2.12 on 2020-04-30 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_auto_20200416_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_city', models.CharField(max_length=30)),
                ('delivery_street', models.CharField(max_length=30)),
                ('delivery_house', models.CharField(max_length=10)),
                ('delivery_apartment', models.PositiveIntegerField(blank=True)),
                ('delivery_options', models.CharField(choices=[('PICK_UP', 'Pick up'), ('COURIER', 'Courier'), ('NOVA_POSHTA', 'Nova Poshta')], default='PICK_UP', max_length=20)),
                ('delivery_comment', models.TextField(blank=True, max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
