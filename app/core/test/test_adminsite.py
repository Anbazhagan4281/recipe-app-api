from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
class AdminSiteTest(TestCase):
    """Testing Admin site"""
    def setUp(self):
        self.client = Client()
        # create super user
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='test123',
        )
        # login
        self.client.force_login(self.admin_user)

        """create test user"""
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='test123',
            name='Test'
        )

    def test_users_list(self):
        """Test that users are listed in site"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

