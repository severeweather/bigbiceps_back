from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/auth/register/"

    def test_register_success(self):
        response = self.client.post(self.url, {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        })

        self.assertEqual(response.status_code, 200)

        user_exists = User.objects.filter(username="testuser").exists()
        self.assertTrue(user_exists)

        user = User.objects.get(username="testuser")
        self.assertNotEqual(user.password, "StrongPass123")
        self.assertTrue(user.check_password("StrongPass123"))