import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from store.models import Product

from .cart import Cart

def api_add_to_cart(request):
    data = json.loads(request.body)
    json_response = {'message': 'Success'}
    product_id = data['product_id']
    quantity = data.get('quantity', 1)

    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id)
    cart.add(product, product.price, quantity)

    return JsonResponse(json_response)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    response = {'message': 'Success'}
    product_id = data['id']

    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)

    return JsonResponse(response)
