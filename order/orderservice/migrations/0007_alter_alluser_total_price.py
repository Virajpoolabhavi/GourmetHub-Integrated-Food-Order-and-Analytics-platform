# Generated by Django 4.2.9 on 2024-03-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderservice', '0006_alter_alluser_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]