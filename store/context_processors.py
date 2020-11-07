"""
Context processors are used to provide custom objects globally to all rendered templates
"""

from .models import Category

def menu_categories(request):
    categories = Category.objects.all();
    return {
        "menu_categories": categories
    }
