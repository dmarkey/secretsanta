from django.db import models
from django.contrib.auth.models import User
import random
import string


class SecretSantaOrg(models.Model):
    key = models.CharField(max_length=256, primary_key=True)
    managing_user = models.ForeignKey(User, related_name="manager")
    secret_santas = models.ManyToManyField(User)
    spending_limit = models.PositiveIntegerField(help_text="The spending limit")
    closing_date = models.DateTimeField(help_text="The last date/time when people can opt-in")
    exchange_date = models.DateTimeField(help_text="The date/time the exchange will take place")
    instructions = models.TextField(help_text="Any additional instructions")

    @staticmethod
    def _create_id():
        char_set = string.ascii_uppercase + string.digits
        return ''.join(random.sample(char_set*6,6))

    def save(self, *args, **kwargs):
        if self.key is None:
            self.key = self._create_id()
        return super(SecretSantaOrg, self).save(*args, **kwargs)
