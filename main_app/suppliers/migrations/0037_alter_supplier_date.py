# Generated by Django 4.0.3 on 2022-05-24 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0036_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 12, 40, 15, 399262), editable=False),
        ),
    ]
