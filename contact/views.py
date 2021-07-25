"""Only the views for the web application"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import ContactFilter
from .forms import ContactForm, AddressForm, PhoneForm, DataForm, AddContactForm
from .logs import logger
from .models import Contact
from .tables import ContactTable


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
                #     # form_b.cleaned_data["primary"] = primary
                #     b = form_b.save(commit=False)
                #     b.contact_id = primary
                #     b.save()
                form_b.save()
            if form_c.is_valid():
                form_c.save()
            if form_d.is_valid():
                form_d.save()
        else:
            logger.error("Form submitted is not valid!")

        return HttpResponseRedirect('/contact/')
    else:
        form = AddContactForm()

    return render(request, 'contact/edit.html', {'form': form})


def update_contact(request) -> object:
    # Modify contact - manual button option
    if request.method == 'POST':
        try:
            obj = Contact.objects.get(pk=request.POST['contact_id'])
            form = ContactForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/contact/')
            else:
                logger.warn("Form submitted is not valid!")
                form.save()
        except Exception:
            # if the data does not already exists, create new entry
            return add_contact(request)

    else:
        form = ContactForm()

    return render(request, 'contact/update.html',
                  {'form': form, 'title': 'Edit Contact'})


def modify_contact(request) -> object:
    # Modify contact - manual button option
    if request.method == 'POST':
        try:
            obj = Contact.objects.get(pk=request.POST['contact_id'])
            form = ContactForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/contact/')
            else:
                logger.warn("Form submitted is not valid!")
                form.save()
        except Exception:
            # if the data does not already exists, create new entry
            return add_contact(request)

    else:
        form = ContactForm()

    return render(request, 'contact/update.html',
                  {'form': form, 'title': 'Edit Contact'})


def delete_contact(request, pk) -> object:
    """
    @param request:
    @return:
    """
    obj = Contact.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/contact/')


# add address

def add_address(request) -> object:
    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
        else:
            logger.error("Form submitted is not valid!")
    else:
        form = AddressForm()

    return render(request, 'contact/edit.html', {'form': form})


# add phone
def add_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
        else:
            logger.error("Form submitted is not valid!")
    else:
        form = PhoneForm()

    return render(request, 'contact/edit.html', {'form': form})


# add date
def add_date(request):
    if request.method == 'POST':
        form = DataForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
        else:
            logger.error("Form submitted is not valid!")
    else:
        form = DataForm()

    return render(request, 'contact/edit.html', {'form': form})
