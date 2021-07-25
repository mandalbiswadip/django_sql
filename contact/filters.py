from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django.db.models import Q
from .models import Contact


class ContactFilter(FilterSet):
    q = CharFilter(method='combined_filter', label='Search')

    class Meta:
        model = Contact
        fields = ['q']

    # custom filter
    def combined_filter(self, queryset, name, value):
        return Contact.objects.filter(
            Q(fname__exact=value) | Q(mname__exact=value) | Q(
                lname__exact=value) | Q(address__state__exact=value) | Q(
                address__address__exact=value) | Q(
                address__city__exact=value) |
            Q(address__zip__exact=value) | Q(
                phone__area_code__exact=value) | Q(phone__number__exact=value)
        ).distinct()
