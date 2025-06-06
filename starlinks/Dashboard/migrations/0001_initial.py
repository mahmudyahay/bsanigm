# Generated by Django 5.1.6 on 2025-05-09 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images')),
                ('status', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.category')),
            ],
        ),
    ]
