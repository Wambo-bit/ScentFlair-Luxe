from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'mary', 'email': 'mary@example.com', 'password': 'M@ryPass123!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        # Register first
        self.client.post(reverse('register'), {'username': 'mary', 'email': 'mary@example.com', 'password': 'M@ryPass123!'}, format='json')
        # Login
        url = reverse('token_obtain_pair')
        data = {'username': 'mary', 'password': 'M@ryPass123!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
