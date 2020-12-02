import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .cart import Cart
from store.models import Product

# Create your views here.
def cart_detail(request):
    cart = Cart(request.session)
    items = list()

    for item in cart:
        items.append({
            'id': item.product.id,
            'product': item.product.title,
            'quantity': item.quantity,
            'price': float(item.price),
            'total_price': float(item.total_price)
        })

    context = {'cart': cart, 'productstring': json.dumps(items)}
    return render(request, 'cart.html', context=context)
