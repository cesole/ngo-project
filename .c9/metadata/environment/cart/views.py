{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":11},{"start":{"row":0,"column":0},"end":{"row":36,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":12},"action":"remove","lines":["quantity"],"id":12},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["d"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["o"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["n"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["a"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["t"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["i"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["o"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":37},"end":{"row":10,"column":45},"action":"remove","lines":["quantity"],"id":13},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["d"]},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"insert","lines":["o"]},{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["n"]},{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["a"]},{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["t"]},{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"insert","lines":["i"]},{"start":{"row":10,"column":43},"end":{"row":10,"column":44},"action":"insert","lines":["o"]},{"start":{"row":10,"column":44},"end":{"row":10,"column":45},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":35},"end":{"row":14,"column":43},"action":"remove","lines":["quantity"],"id":14},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["d"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["o"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["n"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["a"]},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":["t"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["i"]},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["o"]},{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":32},"end":{"row":16,"column":40},"action":"remove","lines":["quantity"],"id":15},{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["d"]},{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["o"]},{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["n"]},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["a"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["t"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["i"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["o"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":12},"action":"remove","lines":["quantity"],"id":16},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["d"]},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["o"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["n"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["a"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["t"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["i"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["o"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":45},"action":"remove","lines":["quantity"],"id":17},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["d"]},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["o"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["n"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["a"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["t"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["i"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["o"]},{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":["n"]}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":15},"action":"remove","lines":["quantity"],"id":18},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["d"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["o"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["n"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["a"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["t"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["i"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["o"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":31,"column":19},"end":{"row":31,"column":27},"action":"remove","lines":["quantity"],"id":19},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["c"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["h"]},{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":["i"]},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["l"]},{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":["d"]},{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":["."]},{"start":{"row":31,"column":25},"end":{"row":31,"column":26},"action":"insert","lines":["i"]},{"start":{"row":31,"column":26},"end":{"row":31,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":31,"column":19},"end":{"row":31,"column":27},"action":"remove","lines":["child.id"],"id":20},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["d"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["o"]},{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":["n"]},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["a"]},{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":["t"]},{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":["i"]},{"start":{"row":31,"column":25},"end":{"row":31,"column":26},"action":"insert","lines":["o"]},{"start":{"row":31,"column":26},"end":{"row":31,"column":27},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":31,"column":27},"end":{"row":31,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572343530818,"hash":"40a238e86cb36e421670ca98b6f7eab34d0b0a6c"}