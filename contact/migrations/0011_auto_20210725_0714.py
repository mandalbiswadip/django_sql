# Generated by Django 3.2.5 on 2021-07-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20210725_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(blank=True, choices=[('home', 'home'), ('work', 'work'), ('', '')], default='home', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
