from django.db import models
from children.models import Child
from django.contrib.auth.models import User


class Order(models.Model):
    full_name = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    date = models.DateField()
    #orderlineitem = models.ForeignKey("OrderLineItem", null=True, blank="false", on_delete=models.CASCADE, related_name="orderlineitem")

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    

class OrderLineItem(models.Model):
    order= models.ForeignKey(Order, null=False, on_delete=models.CASCADE, related_name="order")
    child = models.ForeignKey(Child, null=False, on_delete=models.CASCADE)
    donation = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}".format(
            self.donation, self.child.name)
