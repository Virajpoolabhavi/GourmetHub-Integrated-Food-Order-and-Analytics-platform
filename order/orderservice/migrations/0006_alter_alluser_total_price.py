# Generated by Django 4.2.9 on 2024-03-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderservice', '0005_alluser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='total_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
