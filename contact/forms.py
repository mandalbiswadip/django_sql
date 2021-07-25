from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm, Form

from .models import Contact, Address, Phone, Date


class AddContactForm(Form):
    HOME = "home"
    WORK = "work"
    EMPTY = ""
    contact_id = forms.IntegerField()
    fname = forms.CharField(max_length=15)
    mname = forms.CharField(max_length=15)
    lname = forms.CharField(max_length=15)
    address_type_choice = [(HOME, 'home'), (WORK, 'work'), (EMPTY, "")]
    address_type = forms.CharField(max_length=5,
                                   widget=forms.Select(
                                       choices=address_type_choice),
                                   required=False)
    address = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=12, required=False)
    state = forms.CharField(max_length=6, required=False)
    zip = forms.CharField(max_length=10, required=False)

    HOME = "home"
    WORK = "work"
    CELL = 'cell'
    phone_type_choice = [(HOME, 'home'), (WORK, 'work'), (CELL, 'cell'),
                         (EMPTY, "")]

    phone_type = forms.CharField(max_length=5, widget=forms.Select(
        choices=phone_type_choice),
                                 required=False)

    number = forms.CharField(max_length=12, validators=[], required=False)
    date_type = forms.CharField(max_length=10, required=False)
    date = forms.DateField(required=False)


class ContactForm(ModelForm):
    helper = FormHelper()

    class Meta:
        model = Contact
        fields = ['contact_id', 'fname', 'mname', 'lname']


class AddressForm(ModelForm):
    helper = FormHelper()

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
