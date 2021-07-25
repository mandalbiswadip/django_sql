from django.forms import ModelForm

from .models import Contact, Address, Phone, Date


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_id', 'fname', 'mname', 'lname']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['contact_id', 'address_type', 'address', 'city', 'state',
                  'zip']


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['contact_id', 'phone_type', 'area_code', 'number']


class DataForm(ModelForm):
    class Meta:
        model = Date
        fields = ['contact_id', 'date_type', 'date']
