# Generated by Django 5.0.5 on 2024-05-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('v', models.FloatField(default=0)),
                ('body', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
