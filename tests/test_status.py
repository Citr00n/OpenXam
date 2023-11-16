from django.test import TestCase
from django.test.client import Client

c = Client()


class StatusesTest(TestCase):

    def test_200(self):
        response = c.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = c.get('/404_test/')
        self.assertEqual(response.status_code, 404)
