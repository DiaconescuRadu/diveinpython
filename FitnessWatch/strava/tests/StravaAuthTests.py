from django.urls.base import reverse
from django.test.testcases import TestCase

class StravaAuthTests(TestCase):
    def setUp(self):
        url = reverse('stravaauth')
        self.response = self.client.get(url)
    
    def testStravaAuthStatusCode(self):
        self.assertEquals(self.response.status_code, 200)

    def testStravaAuthContainsStravaHref(self):
        self.assertEquals(self.response.status_code, 200)
        self.assertContains(self.response, 'href="#"')
