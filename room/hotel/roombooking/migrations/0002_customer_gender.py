# Generated by Django 5.0.6 on 2024-08-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=15),
        ),
    ]
