# Generated by Django 4.0.4 on 2022-04-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
