from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/<int:pk>/", views.contact_detail, name="contact_detail"),
    path("contact/add/", views.add_contact, name="add_contact"),
    path("contact/edit/<int:pk>/", views.edit_contact, name="edit_contact"),
    path("contact/delete/<int:pk>/", views.delete_contact, name="delete_contact"),
    path("search/", views.search_contacts, name="search_contacts"),
]
