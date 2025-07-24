from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from account.models import Address


class LoginForm(forms.Form):
            # dar mord mabhase validator ha mitonim ham b shekl pain inaro ba estefade az validator  haye khode jango estefade konim v agr yekam khas tar bashnd mitoniom ba estefade az neveshtan tabe clean braye hame v ya braye tak feild validation error on feild ro baresi konim
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


from django import forms
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        phone = phone.strip().replace(" ", "")

        if len(phone) != 11:
            raise ValidationError("شماره تلفن باید دقیقاً ۱۱ رقم باشد.")

        if not phone.startswith("09"):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")

        if not re.match(r'^\d{11}$', phone):
            raise ValidationError("شماره تلفن باید فقط شامل اعداد باشد.")

        return phone

class AddAddressForm(forms.ModelForm):
    class Meta :
        model = Address
        exclude = ['user']


class RegisterSecondForm(forms.Form):
    code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter your Code'}),)