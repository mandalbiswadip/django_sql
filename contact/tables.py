import django_tables2 as tables
from django_tables2.utils import A

from .models import Contact


class ContactTable(tables.Table):

    delete = tables.TemplateColumn(
        '<form action="/samples/{{record.contact_id}}/delete_contact/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">delete</button></form>',
        orderable=False,
        verbose_name=''
    )

    class Meta:
        model = Contact
        template_name = "django_tables2/bootstrap.html"

        # to select only few columns, fill the following field
        fields = ("contact_id", "fname", "mname", "lname")
