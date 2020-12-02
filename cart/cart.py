from decimal import Decimal

from django.conf import settings

from store.models import Product


class CartItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = Decimal(str(price))
    
    def to_dict(self):
        return {
            'product_id': self.product.pk,
            'quantity': self.quantity,
            'price': str(self.price)
        }


class Cart(object):
    def __init__(self, session):
        self._products_dict = {}
        self.session = session
        self.session_key = settings.CART_SESSION_ID
        if self.session_key in self.session:
            cart = self.session[self.session_key]
            product_ids_in_cart = list(cart.keys())
            product_queryset = self.get_queryset().filter(pk__in=product_ids_in_cart)
            for product in product_queryset:
                product_id = str(product.pk)
                item = cart[product_id]
                self._products_dict[product_id] = CartItem(product, quantity=item['quantity'],
                                                           price=Decimal(item['price']))

    def __iter__(self):
        for item in self._products_dict.values():
            item.total_price = item.price * item.quantity
            yield item

    def add(self, product, price=None, quantity=1):
        """
        Adds or creates product in cart. For an existing product, quantity is increased and the price is ignored
        """
        quantity = int(quantity)
        product_id = str(product.pk)
        if product_id in self._products_dict:
            self._products_dict[product_id].quantity = quantity
        else:
            if price is None:
                raise ValueError('Missing price for new cart item')
            self._products_dict[product_id] = CartItem(product, quantity, price)
        self.update_session()

    def update_session(self):
        """
        Serialize the cart data, saves it to session and marks session as modified.
        """
        self.session[self.session_key] = self.cart_serializable
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.pk)
        if product_id in self._products_dict:
            del self._products_dict[product_id]
            self.update_session()
        else:
            raise ValueError('Given product doesnt exists in cart')

    @staticmethod
    def get_queryset():
        return Product.objects.all()

    @property
    def cart_serializable(self):
        """
        The serializable representation of the cart.
        For instance:
        {
            '1': {'product_id': 1, 'quantity': 2, price: '9.99'},
            '2': {'product_id': 2, 'quantity': 3, price: '29.99'},
        }
        Note how the product pk servers as the dictionary key.
        """
        response = {}
        for item in self._products_dict.values():
            product_id = str(item.product.pk)
            response[product_id] = item.to_dict()
        return response

    @property
    def total_length(self):
        return sum(int(item.quantity) for item in self._products_dict.values())
