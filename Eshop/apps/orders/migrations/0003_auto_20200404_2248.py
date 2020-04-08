# Generated by Django 2.2.4 on 2020-04-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200404_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_payment',
            field=models.CharField(choices=[('Готівка', 'Готівка'), ('Portmone', 'Portmone')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_shipment',
            field=models.CharField(choices=[('Самовивіз', 'Самовивіз'), ('Нова почта', 'Нова почта')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Нове замовлення', 'Нове замовлення'), ('Обробляеться менеджером', 'Обробляеться менеджером'), ('Комплектуэться', 'Комплектуэться'), ('Виконано', 'Виконано')], default='Нове замовлення', max_length=100),
        ),
    ]
