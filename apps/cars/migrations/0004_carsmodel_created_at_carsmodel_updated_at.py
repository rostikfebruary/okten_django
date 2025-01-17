# Generated by Django 5.0.5 on 2024-05-08 09:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carsmodel_price_alter_carsmodel_v_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
