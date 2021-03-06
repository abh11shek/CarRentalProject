# Generated by Django 4.0.1 on 2022-01-15 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='address',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rental_rate',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='car',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='car',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.DeleteModel(
            name='RentalRate',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
