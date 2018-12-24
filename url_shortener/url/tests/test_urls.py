from django.test import TestCase
from django.urls import resolve

from url.views import index, page_redirect


class URLsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Test that the root of the site resolves to the
        correct view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)

    def test_variable_url_uses_index_view(self):
        """
        Test that the root of the site resolves to the
        correct view function
        """
        root = resolve('/1')
        self.assertEqual(root.func, page_redirect)
