# Generated by Django 5.0.6 on 2024-08-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0002_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
