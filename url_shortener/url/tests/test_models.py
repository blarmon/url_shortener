from django.test import TestCase

from url.models import URL

class URLModelTestCase(TestCase):
    def setUp(self):
        self.url = URL.objects.create(
            user_url='https://www.google.com/',
            shortened_url='/1',
            user_email='c.siegel1991@gmail.com',
        )

    def test_url_basic(self):
        """
        Test the basic functionality of Journal
        """
        self.assertEqual(self.url.user_url, 'https://www.google.com/')
        self.assertEqual(self.url.shortened_url, '/1')
        self.assertEqual(self.url.user_email, 'c.siegel1991@gmail.com')
