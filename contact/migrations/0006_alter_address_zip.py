# Generated by Django 3.2.5 on 2021-07-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20210723_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
