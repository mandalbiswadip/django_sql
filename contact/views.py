"""Only the views for the web application"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import ContactFilter
from .forms import ContactForm, AddressForm, PhoneForm, DataForm, \
    AddContactForm, UpdateContactForm, ViewContactForm
from .logs import logger
from .models import Contact, Address, Phone, Date
from .tables import ContactTable
from .validations import normalize_raw_data, normalize_nans


class ContactListView(SingleTableMixin, FilterView):
    model = Contact
    table_class = ContactTable
    template_name = 'contact/contact.html'
    filterset_class = ContactFilter


# add contact
def add_contact(request) -> object:
    logger.warn(request.POST)
    if request.method == 'POST':
        form_a = ContactForm(request.POST)
        form_b = AddressForm(request.POST)
        form_c = PhoneForm(request.POST)
        form_d = DataForm(request.POST)

        if form_a.is_valid():
            form_a.save()

            if form_b.is_valid():
                form_b.save()
            if form_c.is_valid():
                form_c.save()
            if form_d.is_valid():
                form_d.save()
        else:
            logger.warn("Form submitted is not valid!")

        return HttpResponseRedirect('/contact/')
    else:
        form = AddContactForm()

    return render(request, 'contact/edit.html', {'form': form})


def view_contact(request, pk) -> object:
    """
    View contact given contact id
    @param request: request
    @param pk: primary key
    @return: HTTP response
    """
    logger.warn(request.POST)

    obj = Contact.objects.get(pk=pk)

    form = ViewContactForm.from_contact_id(obj)
    return render(request, 'contact/view.html',
                  {'form': form, 'title': 'Edit Contact'})


def update_contact(request, pk) -> object:
    """
    Modify contact - redirect from row
    @param request:
    @param pk:
    @return:
    """
    request_dict = normalize_raw_data(request.POST)
    obj = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form_a = ContactForm(request.POST, instance=obj)
        if form_a.is_valid():
            form_a.save()

        # Saving Address data
        address_objects = Address.objects.filter(
            address_type__exact=request_dict["address_type"],
            contact_id__exact=int(request_dict["contact_id"]))[:1]
        if address_objects.__len__() == 0:
            form_b = AddressForm(request.POST)
        else:
            form_b = AddressForm(request.POST, instance=address_objects[0])
        if form_b.is_valid():
            form_b.save()

        # Saving Phone data
        phone_objects = Phone.objects.filter(
            phone_type__exact=request_dict["phone_type"],
            contact_id__exact=int(request_dict["contact_id"]))[:1]
        if phone_objects.__len__() == 0:
            form_c = PhoneForm(request.POST)
        else:
            form_c = PhoneForm(request.POST, instance=phone_objects[0])
        if form_c.is_valid():
            form_c.save()

        # Saving Date data
        date_objects = Date.objects.filter(
            date_type__exact=request_dict["date_type"],
            contact_id__exact=int(request_dict["contact_id"]))[:1]
        if date_objects.__len__() == 0:
            form_d = DataForm(request.POST)
        else:
            form_d = DataForm(request.POST, instance=date_objects[0])
        if form_d.is_valid():
            form_d.save()

        return HttpResponseRedirect('/contact/')


    else:
        form = UpdateContactForm(initial=normalize_nans(obj.__dict__))

    return render(request, 'contact/update.html',
                  {'form': form, 'title': 'Edit Contact'})


def delete_contact(request, pk) -> object:
    """
    @param request:
    @return:
    """
    Contact.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/contact/')
