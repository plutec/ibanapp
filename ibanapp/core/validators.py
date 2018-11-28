import string

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_iban(value):
    letters = {ord(d): str(i) for i,
               d in enumerate(string.digits + string.ascii_uppercase)}


    def _number_iban(iban):
        return (iban[4:] + iban[:4]).translate(letters)


    def generate_iban_check_digits(iban):
        number_iban = _number_iban(iban[:2] + '00' + iban[4:])
        try:
            return '{:0>2}'.format(98 - (int(number_iban) % 97))
        except ValueError:
            return None


    def valid_iban(iban):
        return int(_number_iban(iban)) % 97 == 1

    if not generate_iban_check_digits(value) == value[2:4] or \
       not valid_iban(value):
        raise ValidationError(
            _('%(value)s is not a valid IBAN'),
            params={'value': value},
        )
