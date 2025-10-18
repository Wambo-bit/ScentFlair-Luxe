from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class OrderTests(APITestCase):
    def test_orders_endpoint_exists(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
