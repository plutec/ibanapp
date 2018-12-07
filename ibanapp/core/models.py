from django.db import models
from django.contrib.auth.models import User

import ibanapp.core.validators

class Account(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    iban = models.CharField(max_length=34,
                            validators=[ibanapp.core.validators.validate_iban])
