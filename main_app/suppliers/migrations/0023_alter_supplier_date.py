# Generated by Django 4.0.3 on 2022-04-22 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0022_alter_supplier_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 16, 38, 52, 227105), editable=False),
        ),
    ]
