{"filter":false,"title":"admin.py","tooltip":"/community/admin.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":3,"column":25},"action":"insert","lines":["from django.contrib import admin","from .models import Post, PostUpVote","","admin.site.register(Post)"]}],[{"start":{"row":1,"column":26},"end":{"row":1,"column":36},"action":"remove","lines":["PostUpVote"],"id":3},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":[" "]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":24},"end":{"row":1,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572871647202,"hash":"a0b1a2729d5fd2a8a7f3387c2bc053ab98f74b9a"}