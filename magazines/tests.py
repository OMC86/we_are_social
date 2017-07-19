from django.test import TestCase
from magazines.views import magazine
from django.core.urlresolvers import resolve


class MagazinePageTest(TestCase):
    def test_magazine_page_resolves(self):
        mag_page = resolve('/magazines/')
        self.assertEqual(mag_page.func, magazine)

    def test_magazine_page_status_code_is_ok(self):
        mag_page = self.client.get('/magazines/')
        self.assertEqual(mag_page.status_code, 302)



# Create your tests here.
