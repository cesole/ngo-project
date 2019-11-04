from django.conf.urls import url
from .views import Contact

urlpatterns = [
    url(r'^$', Contact, name='contact'),
]