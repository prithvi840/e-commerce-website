from django.urls import path

from .views import cart_detail

urlpatterns = [
    path('', cart_detail, name='cart'),
]
