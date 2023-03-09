from django.contrib.auth.models import User
from .models import PrivateScreenshot
from category.models import Category
from rest_framework import status
from rest_framework.test import APITestCase


class PrivateScreenshotDetailViewTests(APITestCase):
    """
    PrivateScreenshot Detail View Testings
    """
    def setUp(self):
        me = User.objects.create_user(username='me', password='me@password')
        category_default1 = Category.objects.create(
            owner=me,
            title='Main',
            
        )
        not_me = User.objects.create_user(username='not_me', password='not_me@password')
        category_default2 = Category.objects.create(
            owner=not_me,
            title='Main',
            
        )
        PrivateScreenshot.objects.create(
            owner=me, 
            title='my first screenshot private', 
            content='This is my very first screenshot', 
            id=1,
            category=category_default1,
        )
        
        PrivateScreenshot.objects.create(
            owner=not_me, 
            title='my first screenshot private', 
            content='This is my very first screenshot', 
            id=2,
            category=category_default2,
        )


    def test_exists_category_when_creating_user(self):
        """
        Testing if a category instance is created when created a User instance
        """
        self.client.login(username='me', password='me@password')
        response = self.client.get('/category/1/')
        self.assertEqual(response.data['title'], 'Main')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_read_category_when_not_logged_user(self):
        """
        Testing to read a category from an other user
        """
        response = self.client.get('/category/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
    def test_read_private_screenshot_not_own_by_user(self):
        """
        Testing to read a private screenshot from an other user
        """
        self.client.login(username='me', password='me@password')
        response = self.client.get('/private-scrshot/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_read_private_screenshot_own_by_user(self):
        """
        Testing to read a private own screenshot 
        """
        self.client.login(username='not_me', password='not_me@password')
        response = self.client.get('/private-scrshot/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)