# Generated by Django 2.1.7 on 2019-04-01 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]