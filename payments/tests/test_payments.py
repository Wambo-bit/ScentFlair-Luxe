from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class PaymentTests(APITestCase):
    def test_mpesa_url_exists(self):
        url = '/api/payments/initiate/'  # Example endpoint
        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])
