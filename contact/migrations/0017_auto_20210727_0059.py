# Generated by Django 3.2.5 on 2021-07-27 00:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_alter_address_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{5}$')]),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{3}-{0,1}\\d{3}-{0,1}\\d{4}$')]),
        ),
    ]