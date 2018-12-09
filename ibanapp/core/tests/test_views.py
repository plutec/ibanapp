from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

from core.models import Account


class ViewsTestCase(TestCase):
    user = None
    account = None

    def setUp(self):
        self.user = User.objects.create(username="Test", email="test@test.com")
        # Create Account with valid IBAN
        self.account = Account.objects.create(created_by=self.user,
                                              first_name="Firstname1",
                                              last_name="Lastname1",
                                              iban="ES1416699352362824876004")

    def test_views_status_code_no_auth(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        response = client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        response = client.get(reverse('account_list'))
        self.assertEqual(response.status_code, 302)
        response = client.get(reverse('account_add'))
        self.assertEqual(response.status_code, 302)
        response = client.get(reverse('account_edit',
                                      kwargs={"account_id":
                                              self.account.id}))
        self.assertEqual(response.status_code, 302)
        response = client.get(reverse('account_delete',
                                      kwargs={"account_id":
                                              self.account.id}))
        self.assertEqual(response.status_code, 302)

    def test_views_status_code_auth(self):
        client_auth = Client()
        client_auth.force_login(user=self.user)

        response = client_auth.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        response = client_auth.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        response = client_auth.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        response = client_auth.get(reverse('account_list'))
        self.assertEqual(response.status_code, 302)
        response = client_auth.get(reverse('account_add'))
        self.assertEqual(response.status_code, 302)
        response = client_auth.get(reverse('account_edit',
                                           kwargs={"account_id":
                                                   self.account.id}))
        self.assertEqual(response.status_code, 302)
        response = client_auth.get(reverse('account_delete',
                                           kwargs={"account_id":
                                                   self.account.id}))
        self.assertEqual(response.status_code, 302)
