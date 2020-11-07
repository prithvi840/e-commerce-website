from django.shortcuts import render, get_object_or_404

from store.models import Product

def frontpage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'frontpage.html', context)

def contactpage(request):
    return render(request, 'contact.html')
