# Generated by Django 5.1.6 on 2025-05-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_products_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default=0, max_length=10000),
            preserve_default=False,
        ),
    ]
