# Generated by Django 3.0.6 on 2020-10-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password_reset_code',
            field=models.CharField(blank=True, default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.BigIntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='town',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]