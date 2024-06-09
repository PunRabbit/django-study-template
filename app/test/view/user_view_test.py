from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.model.snippet import Snippet


class UserViewTest(APITestCase):
    def setUp(self) -> None:
        pass

    def test_get_something(self):
        url = reverse('user')
        response = self.client.get(url)

