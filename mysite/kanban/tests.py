from django.test import TestCase
from django.test.client import Client

# from django.test.client import RequestFactory

# Create your tests here.
class ListViewTest(TestCase):
    print("ListView")
    c = Client()

    response = c.post('/list/', {'order_num': 1})
    print("status_code : {}".format(response.status_code))
