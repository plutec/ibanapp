from django.db import models
from django.contrib.auth.models import User

import core.validators


class Account(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    iban = models.CharField(max_length=34,
                            validators=[core.validators.validate_iban])

    @property
    def complete_name(self):
        return "{} {}".format(self.first_name, self.last_name)
