from django.test import  TestCase, Client
from django.urls import reverse
from webApp.models import Profile
import json

class TestViews(TestCase):

    #Create same client used for each test if have multiple
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.profile_view_url = reverse('profiles_lists')

    #Test for index page
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webApp/index.html')

        #Test to ensure test cases above work fine
        #self.assertEquals(response.status_code, 300)
        #self.assertTemplateUsed(response, 'webApp/incorrectTemplate.html')

    #Test for ProfileList view
    #Quick test to check if URL working, will check rest later if have time
    def test_profile_view_GET(self):
        response = self.client.get(self.profile_view_url)
        self.assertEquals(response.status_code, 200)

