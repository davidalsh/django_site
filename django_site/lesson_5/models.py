from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User


class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(null=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True)
    could_use_int_bouquet = models.BooleanField(default=True)
    wiki_page = models.URLField(default="https://www.wikipedia.org/",
                                name="wikipedia",
                                unique_for_date="delivered_at")
    name = models.CharField(max_length=64, unique=True)


class Bouquet(models.Model):
    fresh_period = models.DurationField(default=timedelta(days=5),
                                        help_text="Use this field when you need to have \
                                        information about bouquet fresh time")
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0)
    flowers = models.ManyToManyField(Flower, verbose_name="This bouquet consists of this flowers")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_email = models.EmailField()
    name = models.CharField(max_length=64)
    invoice = models.FileField()
    user_uuid = models.UUIDField(editable=False)
    discount_size = models.DecimalField(max_digits=10, decimal_places=3)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol="IPv4")
