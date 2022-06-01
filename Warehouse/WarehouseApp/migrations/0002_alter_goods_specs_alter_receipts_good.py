# Generated by Django 4.0.4 on 2022-05-29 19:15

import WarehouseApp.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='specs',
            field=models.FileField(max_length=500, upload_to=WarehouseApp.models.good_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['json'])]),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='good',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='WarehouseApp.supgood', verbose_name='Товар'),
        ),
    ]
