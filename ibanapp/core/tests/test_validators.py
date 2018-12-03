from django.test import TestCase
from core.validators import validate_iban
from django.core.exceptions import ValidationError

class ValidatorTestCase(TestCase):

    def test_validator_iban_correct(self):
        validate_iban("ES1416699352362824876004") #It is OK
    
    def test_validator_iban_incorrect(self):
        with self.assertRaises(ValidationError):
            validate_iban("ES1416699352362824876005") #Invalid IBAN
