import django_tables2 as tables
from .models import Contact


class ContactTable(tables.Table):
    class Meta:
        model = Contact
        template_name = "django_tables2/bootstrap.html"

        # to select only few columns, fill the following field
        # fields = ("contact_id", "fname")
