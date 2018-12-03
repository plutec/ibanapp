from django.test import TestCase
from django.contrib.auth.models import User

from core.models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="Test")
        Account.objects.create(created_by=user,
                               first_name="Firstname1",
                               last_name="Lastname1",
                               iban="ES1416699352362824876004") #Valid IBAN
        Account.objects.create(created_by=user,
                               first_name="Firstname2",
                               last_name="Lastname2",
                               iban="ES1416699352362824876007") #Invalid IBAN
                               # Must be created because the validators only
                               # works with Forms

    def test_accounts_saved(self):
        second_account = Account.objects.get(iban="ES1416699352362824876007")
        first_account = Account.objects.get(first_name="Firstname1")
        self.assertEqual(first_account.iban, "ES1416699352362824876004")
        self.assertEqual(Account.objects.get(first_name="Firstname2"),
                         second_account)
