# Generated by Django 4.0.4 on 2022-06-19 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseApp', '0009_rename_begin_date_emp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='issue_date',
        ),
        migrations.AddField(
            model_name='expenditure',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата получения'),
            preserve_default=False,
        ),
    ]
