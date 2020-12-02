"""
Context processors are used to provide custom objects globally to all rendered templates
"""

from .models import Category
from cart.cart import Cart

def menu_categories(request):
    categories = Category.objects.all();
    cart = Cart(request.session)
    return {
        "menu_categories": categories,
        "cart": cart
    }
