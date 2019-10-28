from django.conf.urls import url, include
from .views import all_children

urlpatterns = [
    url(r'^$', all_children, name='children'),
]