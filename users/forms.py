from django import forms
from .models import FamTamUser
from codes.models import Code


class RegistraitionForm(forms.ModelForm):
    class Meta:
        model = FamTamUser
        fields = ['phone_number']

    def save(self, **kwargs):
        user = FamTamUser(
            phone_number=self.cleaned_data['phone_number']
        )

        user.save()
        return user


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code']
