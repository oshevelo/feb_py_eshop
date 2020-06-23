# Generated by Django 2.2.12 on 2020-06-11 15:40

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20200521_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='status',
            field=django_fsm.FSMField(choices=[('submitted', 'submitted'), ('processing', 'processing'), ('completed', 'completed'), ('suspended', 'suspended'), ('declined', 'declined')], default='submitted', max_length=50),
        ),
    ]
