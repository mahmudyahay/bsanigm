# Generated by Django 5.1.1 on 2025-05-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_customer_shipingadress'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
