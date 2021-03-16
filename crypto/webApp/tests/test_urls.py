from django.test import SimpleTestCase
from django.urls import reverse, resolve
from webApp.views import home

class TestUrls(SimpleTestCase):

    #Test of home URL
    def test_home_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, home)