# Generated by Django 2.2.12 on 2020-05-14 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_merge_20200503_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='discont',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orderitem', to='orders.Order'),
        ),
    ]