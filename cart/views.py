from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    donation = int(request.POST.get('donation'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + donation      
    else:
        cart[id] = cart.get(id, donation) 

    request.session['cart'] = cart
    return redirect(reverse('children'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    donation = int(request.POST.get('donation'))
    cart = request.session.get('cart', {})

    if donation > 0:
        cart[id] = donation
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))