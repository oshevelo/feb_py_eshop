# Generated by Django 2.2.12 on 2020-06-06 18:45

import apps.carts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0012_auto_20200507_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_number',
            field=models.CharField(default=apps.carts.models.Cart.generator, max_length=37, verbose_name='Номер кошика'),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cart_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cart_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='updated on'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Власник'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cartitem_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts_cartitem_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='updated on'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Власник'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart', verbose_name='Номер кошика'),
        ),
    ]