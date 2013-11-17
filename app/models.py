from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime


class SecretSantaOrg(models.Model):
    unique_id = models.CharField(max_length=108, primary_key=True)
    name = models.CharField(max_length=256, help_text="Acme secret santa, for example", blank=False, null=False)
    status = models.CharField(max_length=32, default="NOT_SENT")
    secret_key = models.CharField(max_length=256)
    spending_limit = models.PositiveIntegerField(help_text="The spending limit", blank=False, null=False)
    closing_date = models.DateTimeField(help_text="The last date/time when people can opt-in", blank=False, null=False)
    exchange_date = models.DateTimeField(help_text="The date/time the exchange will take place", blank=False, null=False)
    instructions = models.TextField(help_text="Any additional instructions", blank=False, null=False)

    @property
    def open_for_registration(self):
        return datetime.datetime.now() < self.closing_date

    @property
    def exchange_done(self):
        return datetime.datetime.now() > self.exchange_date

    @property
    def get_status(self):
        if self.exchange_done:
            return "Complete"
        if self.status == "SENT":
            return "Secret santa emails have been sent. Get shopping!"
        if not self.open_for_registration:
            return "Currently not open for registration, look out for an email!"
        return "Currently accepting registrations"

    def get_participants(self):
        return self.participant_set.all()

    def add_participant(self, email):
        if not self.participant_set.all().filter(email=email):
            Participant(email=email, org=self).save()

    def save(self, *args, **kwargs):
        if self.unique_id == '':
            unique_id = str(uuid.uuid4()) + str(uuid.uuid4()) + str(uuid.uuid4())
            self.unique_id = unique_id.replace("-", "")
        if self.secret_key == '':
            self.secret_key = User.objects.make_random_password(length=16)
        super(SecretSantaOrg, self).save(*args, **kwargs)


class Participant(models.Model):
    email = models.EmailField()
    secret_key = models.CharField(max_length=500)
    org = models.ForeignKey(SecretSantaOrg)

    def save(self, *args, **kwargs):
        if self.secret_key == "":
            self.secret_key = User.objects.make_random_password(length=16)
        super(Participant, self).save(*args, **kwargs)