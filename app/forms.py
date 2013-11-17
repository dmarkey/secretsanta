__author__ = 'dmarkey'
from models import SecretSantaOrg
from captcha.fields import CaptchaField
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User


class NewSecretSantaForm(forms.ModelForm):
    your_email = forms.EmailField(max_length=256)
    captcha = CaptchaField()

    def clean(self):
        cleaned_data = super(NewSecretSantaForm, self).clean()
        if self.errors:
            return cleaned_data
        if cleaned_data['closing_date'] > cleaned_data['exchange_date']:
            raise forms.ValidationError("Closing date is after the exchange date")
        return cleaned_data


    class Meta:
        model = SecretSantaOrg
        exclude = ("participants", "unique_id", "status", "secret_key")
        widgets = {
            'exchange_date': DateTimeWidget,
            'closing_date': DateTimeWidget,
        }



class RegisterForm(forms.Form):
    your_email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if self.errors:
            return cleaned_data

        email = cleaned_data['your_email']
        if self.org.get_participants().filter(email=email):
            raise forms.ValidationError("You have already registered!")
        return cleaned_data;

    def set_org(self, org):
        self.org = org;







