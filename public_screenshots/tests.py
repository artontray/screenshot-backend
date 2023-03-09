from django.contrib.auth.models import User
from .models import PublicScreenshot
from rest_framework import status
from rest_framework.test import APITestCase


class PublicScreenshotDetailViewTests(APITestCase):
    """
    PublicScreenshot Detail View Testings
    """
    def setUp(self):
        me = User.objects.create_user(username='me', password='me@password')
        not_me = User.objects.create_user(username='not_me', password='not_me@password')
        PublicScreenshot.objects.create(
            owner=me, title='my first screenshot', content='This is my very first screenshot', id=1
        )
        PublicScreenshot.objects.create(
            owner=not_me, title='my first screenshot', content='This is my very first screenshot', id=2
        )


    def test_read_screenshot(self):
        """
        Testing a user reading a screenshot
        """
        response = self.client.get('/public-scrshot/1/')
        self.assertEqual(response.data['title'], 'my first screenshot')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_read_screenshot_with_invalid_id(self):
        """
        Testing a user reading a screenshot using an invalid ID
        """
        response = self.client.get('/public-scrshot/99999999/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_own_screenshot(self):
        """
        Testing a user deleting a own screenshot 
        """
        self.client.login(username='me', password='me@password')
        response = self.client.delete('/public-scrshot/1/', format='json')
        response = self.client.get('/public-scrshot/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_own_screenshot(self):
        """
        Testing a user updating a own screenshot 
        """
        self.client.login(username='me', password='me@password')
        response = self.client.put('/public-scrshot/1/', {
          'owner': 'me', 'title': 'new title'
        }, format='json')
        publicscreenshot =  PublicScreenshot.objects.filter(pk=1).first()
        self.assertEqual(publicscreenshot.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_not_own_screenshot(self):
        """
        Testing a user updating a screenshot from other user
        """
        self.client.login(username='me', password='me@password')
        response = self.client.put('/public-scrshot/2/', {
            'title': 'a new title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)