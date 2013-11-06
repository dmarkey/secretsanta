from django.db import models
from django.contrib.auth.models import User
import random
import string


class SecretSantaOrg(models.Model):
    key = models.CharField(max_length=256, primary_key=True)
    managing_user = models.ForeignKey(User, related_name="manager")
    secret_santas = models.ManyToManyField(User)
    spending_limit = models.IntegerField()
    due_date = models.DateTimeField()
    instructions = models.TextField()

    @staticmethod
    def _create_id():
        char_set = string.ascii_uppercase + string.digits
        return ''.join(random.sample(char_set*6,6))

    def save(self, *args, **kwargs):
        if self.key is None:
            self.key = self._create_id()
        return super(SecretSantaOrg, self).save(*args, **kwargs)
