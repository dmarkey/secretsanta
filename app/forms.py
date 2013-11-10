__author__ = 'dmarkey'
from models import SecretSantaOrg

from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User


class NewSecretSantaForm(forms.ModelForm):
    your_email = forms.EmailField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput(), help_text="If you have used this before, your current password, If you are a new user, enter a simple password.")

    def clean(self):
        cleaned_data = super(NewSecretSantaForm, self).clean()
        if self.errors:
            return cleaned_data

        try:
            user = User.objects.get(email=cleaned_data['your_email'])
            if not user.check_password(cleaned_data['password']):
                raise forms.ValidationError("Password incorrect")
            pass
        except User.DoesNotExist:
            pass

        if cleaned_data['closing_date'] > cleaned_data['exchange_date']:
            raise forms.ValidationError("Closing date is after the exchange date")
        return cleaned_data

    def save(self, commit=True):
        user, created = User.objects.get_or_create(email=self.cleaned_data['your_email'], username=self.cleaned_data['your_email'])
        if created:
            user.set_password(self.cleaned_data['password'])
            user.save()
        self.instance.managing_user = user
        return super(NewSecretSantaForm, self).save(commit=True)


    class Meta:
        model = SecretSantaOrg
        exclude = ("managing_user", "participants", "unique_id", "status")
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
        if email in self.org.get_participants():
            raise forms.ValidationError("You have already registered!")
        return cleaned_data;

    def set_org(self, org):
        self.org = org;







