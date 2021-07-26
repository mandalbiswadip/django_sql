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
            Q(fname__icontains=value) | Q(mname__icontains=value) | Q(
                lname__icontains=value) | Q(address__state__icontains=value) | Q(
                address__address__icontains=value) | Q(
                address__city__icontains=value) |
            Q(address__zip__exact=value) | Q(
                phone__area_code__exact=value) | Q(phone__number__icontains=value)
        ).distinct()
