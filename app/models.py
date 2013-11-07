from django.db import models
from django.contrib.auth.models import User
import random
import string


class SecretSantaOrg(models.Model):
    name = models.CharField(max_length=256, primary_key=True, help_text="Acme secret santa, for example")
    managing_user = models.ForeignKey(User, related_name="manager")
    secret_santas = models.ManyToManyField(User)
    spending_limit = models.PositiveIntegerField(help_text="The spending limit")
    closing_date = models.DateTimeField(help_text="The last date/time when people can opt-in")
    exchange_date = models.DateTimeField(help_text="The date/time the exchange will take place")
    instructions = models.TextField(help_text="Any additional instructions")

    def save(self, *args, **kwargs):
        if self.key is None:
            self.key = self._create_id()
        return super(SecretSantaOrg, self).save(*args, **kwargs)
