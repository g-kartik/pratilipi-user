from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class LipiUserAPITestCase(APITestCase):

    def test_create_lipi_user(self):
        """
        Ensure create user api is working
        """
        data = {'first_name': 'lipi_first_1', 'last_name': 'lipi_last_1', 'email': 'lipi_user_1@gmail.com',
                'phone_number': '9576254624'}
        response = self.client.post(reverse('user-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)