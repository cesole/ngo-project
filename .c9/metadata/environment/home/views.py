{"filter":false,"title":"views.py","tooltip":"/home/views.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["e"],"id":2},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["m"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["o"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["h"]}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["i"],"id":3},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["n"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["d"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["e"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["x"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":8},"action":"remove","lines":["home"],"id":4},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["i"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["n"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["d"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["e"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["x"]}],[{"start":{"row":0,"column":0},"end":{"row":15,"column":37},"action":"remove","lines":["from django.shortcuts import render","from django.core.mail import send_mail","from django.conf import settings","","","def index(request):","","#\tif request.method == 'POST':","#\t\tmessage = request.POST['message']","#","#\t\tsend_mail('Contact Form',","#\t\t message, ","#\t\t settings.EMAIL_HOST_USER,","#\t\t ['ivanovsin11@gmail.com'], ","#\t\t fail_silently=False)","\treturn render(request, 'index.html')"],"id":5},{"start":{"row":0,"column":0},"end":{"row":4,"column":40},"action":"insert","lines":["from django.shortcuts import render","","# Create your views here.","def index(request):","    return render(request, \"index.html\")"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":40},"end":{"row":4,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572627009266,"hash":"d349dcef1b2d0fcacd50cca345ee8529e7bb642c"}