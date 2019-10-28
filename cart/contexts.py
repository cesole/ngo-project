from django.shortcuts import get_object_or_404
from children.models import Child


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    child_count = 0
    
    for id, donation in cart.items():
        child = get_object_or_404(Child, pk=id)
        total += donation * child.price
        child_count += quantity
        cart_items.append({'id': id, 'donation': quantity, 'child': child})
    
    return {'cart_items': cart_items, 'total': total, 'child_count': child_count}