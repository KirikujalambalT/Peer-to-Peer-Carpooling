# Generated by Django 4.1.7 on 2023-05-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_booking_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=80),
        ),
    ]
