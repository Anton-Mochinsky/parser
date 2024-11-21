from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "testuser1",
            "email": "testuser1@example.com",
            "password": "password123!!",
            "password2": "password123!!",
        }
        response = self.client.post('/api/accounts/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        User.objects.create_user(username="testuser1", email="testuser1@example.com", password="password123!!")
        data = {
            "username": "testuser1",
            "password": "password123!!"
        }
        response = self.client.post('/api/accounts/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_part_search(self):
        user = User.objects.create_user(username="testuser1", email="testuser1@example.com", password="password123!!")
        self.client.force_authenticate(user)
        response = self.client.get('/api/accounts/search/12345ABC/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('part_number', response.data)
