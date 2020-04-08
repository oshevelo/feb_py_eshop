# Generated by Django 2.2.4 on 2020-04-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Нове замовлення', 'Нове замовлення'), ('Обробляеться менеджером', 'Обробляеться менеджером'), ('Комплектуэться', 'Комплектуэться'), ('Виконано', 'Виконано')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
