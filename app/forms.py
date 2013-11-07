__author__ = 'dmarkey'
from models import SecretSantaOrg

from django import forms
from datetimewidget.widgets import DateTimeWidget


class NewSecretSantaForm(forms.ModelForm):
    class Meta:
        model = SecretSantaOrg
        exclude = ("key", "managing_user", "secret_santas")
        widgets = {
            'exchange_date': DateTimeWidget,
            'closing_date': DateTimeWidget,
        }


