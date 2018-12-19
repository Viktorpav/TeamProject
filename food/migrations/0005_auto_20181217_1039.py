# Generated by Django 2.1.3 on 2018-12-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
