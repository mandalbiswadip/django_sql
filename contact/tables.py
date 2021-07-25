import django_tables2 as tables
from django_tables2.utils import A

from .models import Contact


class ContactTable(tables.Table):

    delete = tables.TemplateColumn(
        '<form action="/samples/{{record.contact_id}}/delete_contact/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">delete</button></form>',
        orderable=False,
        verbose_name=''
    )

    update = tables.TemplateColumn(
        '<form action="/samples/{{record.contact_id}}/update_contact/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="update"><button data-toggle="tooltip" title="Update row" type="submit" class="btn btn-danger btn-xs">Update</button></form>',
        orderable=False,
        verbose_name=''
    )

    view = tables.TemplateColumn(
        '<form action="/samples/{{record.contact_id}}/view_contact/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="update"><button data-toggle="tooltip" title="View row" type="submit" class="btn btn-danger btn-xs">View</button></form>',
        orderable=False,
        verbose_name=''
    )

    class Meta:
        model = Contact
        template_name = "django_tables2/bootstrap.html"

        # to select only few columns, fill the following field
        fields = ("contact_id", "fname", "mname", "lname")
