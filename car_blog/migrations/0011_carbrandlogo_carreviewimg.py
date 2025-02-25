# Generated by Django 5.1.6 on 2025-02-25 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_blog', '0010_rename_brand_carbrand_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrandLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_logo', models.ImageField(blank=True, upload_to='car_logo')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_logo', to='car_blog.carbrand')),
            ],
        ),
        migrations.CreateModel(
            name='CarReviewImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_img', models.ImageField(blank=True, upload_to='car_img')),
                ('car_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_img', to='car_blog.carreview')),
            ],
        ),
    ]
