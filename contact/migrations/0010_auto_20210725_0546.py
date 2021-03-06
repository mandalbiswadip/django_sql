# Generated by Django 3.2.5 on 2021-07-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_alter_contact_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(blank=True, choices=[('home', 'home'), ('work', 'work')], default='home', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mname',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='date_type',
            field=models.CharField(blank=True, default='birth', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='area_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_type',
            field=models.CharField(blank=True, choices=[('home', 'home'), ('work', 'work'), ('cell', 'cell')], default='cell', max_length=5, null=True),
        ),
    ]
