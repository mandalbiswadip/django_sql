"""
Parse csv dataset and store the data in SQL tables
"""
import os

import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manage_contact.settings')
django.setup()

from contact import models
from tqdm import tqdm

from contact.validations import validate_nan as validate, normalize_nans


# parse a single row and store in appropriate tables
def parse_row(row: pd.Series) -> None:
    # don't allow nan values anywhere
    row = normalize_nans(row)

    contact = models.Contact(contact_id=row.contact_id,
                             fname=row.first_name, mname=row.middle_name,
                             lname=row.last_name)
    contact.save()

    # don't add address if all entities are empty
    if any([validate(row.home_address), validate(row.home_city),
            validate(row.home_state), validate(row.home_zip)]):
        address = models.Address(contact_id=contact,
                                 address_type="home",
                                 address=row.home_address,
                                 city=row.home_city, state=row.home_state,
                                 zip=None if not validate(
                                     row.home_zip) else str(int(row.home_zip)))
        address.save()

    if any([validate(row.work_address), validate(row.work_city),
            validate(row.work_state), validate(row.work_zip)]):
        address = models.Address(contact_id=contact,
                                 address_type="work",
                                 address=row.work_address,
                                 city=row.work_city, state=row.work_state,
                                 zip=None if not validate(
                                     row.home_zip) else str(int(row.home_zip)))
        address.save()

    if validate(row.home_phone):
        phone = models.Phone(contact_id=contact, phone_type='home',
                             number=row.home_phone)
        phone.save()

    if validate(row.cell_phone):
        phone = models.Phone(contact_id=contact, phone_type='cell',
                             number=row.cell_phone)
        phone.save()

    if validate(row.work_phone):
        phone = models.Phone(contact_id=contact, phone_type='work',
                             number=row.work_phone)
        phone.save()

    if validate(row.birth_date):
        dt = models.Date(contact_id=contact, date_type="birth",
                         date=row.birth_date)
        dt.save()


data = pd.read_csv("../Contacts.cvs.csv")

for index, row in tqdm(data.iterrows()):
    parse_row(row)
