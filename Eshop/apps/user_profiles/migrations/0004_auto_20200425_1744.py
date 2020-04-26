# Generated by Django 2.2.12 on 2020-04-25 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_auto_20200424_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaddress',
            name='apartment_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='house_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='street',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profiles.UserProfile'),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='zip_code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='region',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
    ]