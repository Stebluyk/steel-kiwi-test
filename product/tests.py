import datetime
from django.utils import timezone
from django.test import TestCase
from product.models import Product


future_adding = Product(created_at=timezone.now()+ datetime.timedelta(days=30))

future_adding.was_published_recently()


class TestForProductAddingTime(TestCase):

    def product_was_added_recently_in_future(self):
        time  = timezone.now() + datetime.timedelta(days=30)
        future_adding = Product(created_at=time)

self.asserEqual(future_adding.was_published_recently(),False)