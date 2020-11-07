from django.urls import path

from .views import front_page, about_page, contact_page


urlpatterns = [
    path('', front_page, name='frontpage'),
    path('contact', contact_page, name='contact'),
    path('about', about_page, name='about')
]
