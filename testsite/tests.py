# testsite/tests.py
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

class AboutPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(True,False)