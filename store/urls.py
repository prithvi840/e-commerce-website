from django.urls import path

from .views import product_detail, category_detail

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail')
]

