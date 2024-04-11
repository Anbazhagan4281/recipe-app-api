"""
Test for Models
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

class ModelTest(TestCase):
    """Testing Models"""
    def test_create_user_model_with_email_successfull(self):
        email = "test@example.com"
        password = "test"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_check_email_normalize(self):
        test_emails = [
            ['example1@Example.com', 'example1@example.com'],
            ['Example3@example.com', 'Example3@example.com'],
            ['EXAMPLE4@EXAMPLE.com', 'EXAMPLE4@example.com'],
        ]
        
        for email, excepted in test_emails:
            user = get_user_model().objects.create_user(email, password='test123')
            self.assertEqual(user.email, excepted)

    
    def test_check_email_is_required(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_check_user_is_superuser(self):
        user = get_user_model().objects.create_superuser(email='test@example.com', password='test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.id_staff)