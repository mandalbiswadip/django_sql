"""All models required by the given schema"""
from django.db import models

from . import validations
from .logs import logger


class Contact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=15)
    mname = models.CharField(max_length=15, blank=True)
    lname = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.fname


class Address(models.Model):
    HOME = "home"
    WORK = "work"
    EMPTY = ""
    address_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(to=Contact, on_delete=models.CASCADE,
                                   db_column='contact_id')
    address_type_choice = [(HOME, 'home'), (WORK, 'work')]
    address_type = models.CharField(max_length=5, choices=address_type_choice,
                                    default=HOME)
    address = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=12, null=True, blank=True)
    state = models.CharField(max_length=6, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.address_id


class Phone(models.Model):
    HOME = "home"
    WORK = "work"
    CELL = 'cell'
    phone_type_choice = [(HOME, 'home'), (WORK, 'work'), (CELL, 'cell')]

    phone_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(to=Contact, on_delete=models.CASCADE,
                                   db_column='contact_id')
    # TODO provide choice
    phone_type = models.CharField(max_length=5, choices=phone_type_choice,
                                  default=CELL)
    area_code = models.CharField(max_length=3, null=True, blank=True)

    def val_number(self, x):
        return validations.validate_len(x, 12, field='number')

    # TODO validate number format
    # TODO validation error resolve
    number = models.CharField(max_length=12, validators=[], null=True,
                              blank=True)

    # TODO check validity
    def save(self, *args, **kwargs):
        try:
            self.area_code = str(self.number[:3])
        except Exception:
            logger.warn("Number failed to parse for area code")
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone_id


class Date(models.Model):
    date_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(to=Contact, db_column='contact_id',
                                   on_delete=models.CASCADE)
    # include date_type
    date_type = models.CharField(max_length=10, default='birth')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.date_id
