# Generated by Django 5.0.5 on 2024-05-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carsmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='v',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='year',
            field=models.IntegerField(),
        ),
    ]
