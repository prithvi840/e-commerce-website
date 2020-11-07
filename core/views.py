from django.shortcuts import render, get_object_or_404

from store.models import Product

def front_page(request):
    products = Product.objects.filter(is_featured=True)
    context = {
        'products': products
    }
    return render(request, 'frontpage.html', context)

def contact_page(request):
    return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')
