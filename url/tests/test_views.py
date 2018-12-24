from django.test import TestCase
from django.urls import reverse

from url.views import index


class IndexViewTestCase(TestCase):

    def test_index_view(self):
        """
        Test that the index view returns a 200 response and uses the correct template
        """
        with self.assertTemplateUsed('url/index.html'):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 200)
