# Generated by Django 5.0.3 on 2024-03-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_category_product_active_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='total',
        ),
        migrations.AddField(
            model_name='sales',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
