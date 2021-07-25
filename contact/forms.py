from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm, Form

from .models import Contact, Address, Phone, Date
from .validations import normalize_nans


class ViewContactForm(Form):
    HOME = "home"
    WORK = "work"
    EMPTY = ""
    contact_id = forms.IntegerField(disabled=True)
    fname = forms.CharField(max_length=15, disabled=True)
    mname = forms.CharField(max_length=15, disabled=True)
    lname = forms.CharField(max_length=15, disabled=True)
    home_address = forms.CharField(max_length=30, disabled=True)
    home_city = forms.CharField(max_length=12, disabled=True)
    home_state = forms.CharField(max_length=6, disabled=True)
    home_zip = forms.CharField(max_length=10, disabled=True)

    work_address = forms.CharField(max_length=30, disabled=True)
    work_city = forms.CharField(max_length=12, disabled=True)
    work_state = forms.CharField(max_length=6, disabled=True)
    work_zip = forms.CharField(max_length=10, disabled=True)

    work_number = forms.CharField(max_length=12, disabled=True)
    work_area_code = forms.CharField(max_length=12, disabled=True)

    home_number = forms.CharField(max_length=12, disabled=True)
    home_area_code = forms.CharField(max_length=12, disabled=True)

    cell_number = forms.CharField(max_length=12, disabled=True)
    cell_area_code = forms.CharField(max_length=12, disabled=True)

    birth_date = forms.DateField(disabled=True)

    @classmethod
    def from_contact_id(cls, contact_object):
        data = {
            "contact_id": contact_object.pk,
            "fname": contact_object.fname,
            "mname": contact_object.mname,
            "lname": contact_object.lname,
        }

        # View addresses
        for address_type in ["home", "work"]:
            address_objects = Address.objects.filter(
                address_type__exact=address_type,
                contact_id__exact=int(contact_object.pk))[:1]
            if len(address_objects) == 0:
                data.update({
                    "{}_address".format(address_type): "",
                    "{}_city".format(address_type): "",
                    "{}_state".format(address_type): "",
                    "{}_zip".format(address_type): ""
                })
            else:
                address_object = address_objects[0]
                data.update({
                    "{}_address".format(address_type): address_object.address,
                    "{}_city".format(address_type): address_object.city,
                    "{}_state".format(address_type): address_object.state,
                    "{}_zip".format(address_type): address_object.zip
                })

        for phone_type in ["home", "work", "cell"]:
            phone_objects = Phone.objects.filter(
                phone_type__exact=phone_type,
                contact_id__exact=int(contact_object.pk))[:1]
            if len(phone_objects) == 0:
                data.update({
                    "{}_number".format(phone_type): "",
                    "{}_area_code".format(phone_type): "",
                })
            else:
                phone_object = phone_objects[0]
                data.update({
                    "{}_number".format(phone_type): phone_object.number,
                    "{}_area_code".format(phone_type): phone_object.area_code,
                })

        for d_type in ["birth"]:
            date_objects = Date.objects.filter(
                date_type__exact=d_type,
                contact_id__exact=int(contact_object.pk))[:1]
            if len(date_objects) == 0:
                data.update({
                    "{}_date".format(d_type): "",
                })
            else:
                date_object = date_objects[0]
                data.update({
                    "{}_date".format(d_type): date_object.date,
                })
        data = normalize_nans(data)

        return cls(initial=data)


class AddContactForm(Form):
    HOME = "home"
    WORK = "work"
    EMPTY = ""
    contact_id = forms.IntegerField()
    fname = forms.CharField(max_length=15)
    mname = forms.CharField(max_length=15, required=False)
    lname = forms.CharField(max_length=15, required=False)
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
    date = forms.DateField(required=False, initial="MM/DD/YYYY")


class UpdateContactForm(Form):
    """form for updating contacts"""
    HOME = "home"
    WORK = "work"
    EMPTY = ""
    contact_id = forms.IntegerField()
    fname = forms.CharField(max_length=15, required=False)
    mname = forms.CharField(max_length=15, required=False)
    lname = forms.CharField(max_length=15, required=False)
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
    date = forms.DateField(required=False, initial="MM/DD/YYYY")


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
