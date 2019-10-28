{"filter":false,"title":"urls.py","tooltip":"/ngo/urls.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":15,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]"],"id":2},{"start":{"row":15,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from checkout import urls as urls_checkout","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}],[{"start":{"row":18,"column":5},"end":{"row":18,"column":13},"action":"remove","lines":["products"],"id":3},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["c"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["h"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["i"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["l"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["d"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["r"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["e"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":34},"end":{"row":18,"column":42},"action":"remove","lines":["products"],"id":4},{"start":{"row":18,"column":34},"end":{"row":18,"column":35},"action":"insert","lines":["c"]},{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"insert","lines":["h"]},{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"insert","lines":["i"]},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["l"]},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["d"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["r"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["e"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":19},"action":"remove","lines":["products"],"id":5},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["c"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["h"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["i"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["l"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["d"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["r"]},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"insert","lines":["e"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":30,"column":36},"end":{"row":30,"column":44},"action":"remove","lines":["products"],"id":6},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"insert","lines":["c"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"insert","lines":["h"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"insert","lines":["i"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"insert","lines":["l"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":["d"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":["r"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["e"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":13},"action":"remove","lines":["products"],"id":7},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["c"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["h"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["i"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["l"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["d"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["r"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["e"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":39},"action":"remove","lines":["products"],"id":8},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["c"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["h"]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["i"]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["l"]},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["d"]},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["r"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["e"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":27},"action":"remove","lines":["products"],"id":9},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["c"]},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["h"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["i"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["l"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["d"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["r"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["e"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["·"],"id":11}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["·"],"id":12}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["#"],"id":13}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["#"],"id":15}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["#"],"id":16}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["#"],"id":17}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["#"],"id":18}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":["#"],"id":19}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["#"],"id":20}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["#"],"id":21}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["#"],"id":22}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["#"],"id":23}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["#"],"id":24}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["#"],"id":25}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"remove","lines":["#"],"id":27}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["#"],"id":28}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"remove","lines":["#"],"id":29}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["#"],"id":30}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["#"],"id":31}],[{"start":{"row":23,"column":31},"end":{"row":24,"column":0},"action":"remove","lines":["",""],"id":32}],[{"start":{"row":23,"column":31},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":33}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":["#"],"id":34}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"remove","lines":["#"],"id":35}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["#"],"id":36}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["#"],"id":37}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"remove","lines":["#"],"id":38}]]},"ace":{"folds":[],"scrolltop":176.484375,"scrollleft":0,"selection":{"start":{"row":31,"column":4},"end":{"row":31,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":13,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1572263905692,"hash":"7d2fd24244ad0b72eeafc8f45fee4f21b3cb4e52"}