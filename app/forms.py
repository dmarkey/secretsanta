__author__ = 'dmarkey'
from models import SecretSantaOrg

from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User


class NewSecretSantaForm(forms.ModelForm):
    your_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), help_text="If you have used this before, your current password, If you are a new user, enter a simple password.")

    def save(self, commit=True):
        user, created = User.objects.get_or_create(email=self.cleaned_data['your_email'])
        if created:
            user.set_password(self.cleaned_data['password'])
            user.save()
        self.instance.managing_user = user
        return super(NewSecretSantaForm, self).save(commit=True)


    class Meta:
        model = SecretSantaOrg
        exclude = ("managing_user", "secret_santas")
        widgets = {
            'exchange_date': DateTimeWidget,
            'closing_date': DateTimeWidget,
        }




