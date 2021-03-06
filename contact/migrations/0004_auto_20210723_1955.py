# Generated by Django 3.2.5 on 2021-07-23 19:55

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210723_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='date_type',
            field=models.CharField(default='birth', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='area_code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=12, null=True, validators=[contact.models.Phone.val_number]),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_type',
            field=models.CharField(choices=[('home', 'home'), ('work', 'work'), ('cell', 'cell')], default='cell', max_length=5, null=True),
        ),
    ]
