__author__ = 'dmarkey'
from models import SecretSantaOrg
from bootstrap_toolkit.widgets import BootstrapDateInput

from django import forms

class NewSecretSantaForm(forms.ModelForm):
    class Meta:
        model = SecretSantaOrg
        exclude = ("key", "managing_user", "secret_santas")
        widgets = {
            'due_date': BootstrapDateInput,
        }


