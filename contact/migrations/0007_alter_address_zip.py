# Generated by Django 3.2.5 on 2021-07-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_address_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=10, null=True),
        ),
    ]