# Generated by Django 5.1.6 on 2025-02-19 18:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_blog', '0005_rename_horsepower_carreview_horsepower_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreview',
            name='fuel',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=10), blank=True, default=True, size=None),
        ),
    ]
