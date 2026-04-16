from django.urls import path
from .views import contact_view, contact_success_view

app_name = "contacts"

urlpatterns = [
    path('create/', contact_view, name='create'),
    path('create_contact/', contact_view, name='create_contact'),
    path('contact_success/', contact_success_view, name='contact_success'),
]