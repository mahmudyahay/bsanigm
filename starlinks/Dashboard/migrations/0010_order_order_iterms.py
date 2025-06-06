# Generated by Django 5.1.1 on 2025-05-23 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0009_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('ORDERED', 'ORDERED'), ('SHIPPED', 'SHIPPED'), ('DELIVERD', 'DELIVERD')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.customer')),
            ],
        ),
        migrations.CreateModel(
            name='order_iterms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.products')),
            ],
        ),
    ]
