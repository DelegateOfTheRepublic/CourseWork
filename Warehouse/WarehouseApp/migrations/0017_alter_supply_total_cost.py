# Generated by Django 4.0.4 on 2022-06-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseApp', '0016_alter_supstring_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='total_cost',
            field=models.DecimalField(decimal_places=5, max_digits=12, verbose_name='Конечная цена'),
        ),
    ]
