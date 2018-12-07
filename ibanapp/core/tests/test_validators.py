from django.test import TestCase
from django.core.exceptions import ValidationError

from ibanapp.core.validators import validate_iban


class ValidatorTestCase(TestCase):

    def test_validator_iban_correct(self):
        self.assertEqual(validate_iban("ES1416699352362824876004"),
                         "ES1416699352362824876004")

    def test_validator_iban_incorrect(self):
        with self.assertRaises(ValidationError):
            validate_iban("ES1416699352362824876005")  # Invalid IBAN
