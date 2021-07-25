"""manage_contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactListView.as_view()),
    path(r'add_contact/', views.add_contact),
    path(r'modify_contact/', views.modify_contact),
    url(r'^samples/(?P<pk>\d+)/delete_contact/$', views.delete_contact,
        name='Delete Contact'),
    path(r'address/', views.add_address),
    path(r'phone/', views.add_phone),
    path(r'date/', views.add_date),
]
