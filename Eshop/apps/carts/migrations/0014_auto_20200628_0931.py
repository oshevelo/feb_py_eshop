# Generated by Django 2.2.12 on 2020-06-28 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_auto_20200606_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cart_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Коли створено'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cart_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cartitem_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Коли створено'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cartitem_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
    ]
