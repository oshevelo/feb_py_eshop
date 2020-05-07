from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200417_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
