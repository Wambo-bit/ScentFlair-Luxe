from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class ProductTests(APITestCase):
    def test_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
