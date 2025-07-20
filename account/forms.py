from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

class LoginForm(forms.Form):
            # dar mord mabhase validator ha mitonim ham b shekl pain inaro ba estefade az validator  haye khode jango estefade konim v agr yekam khas tar bashnd mitoniom ba estefade az neveshtan tabe clean braye hame v ya braye tak feild validation error on feild ro baresi konim
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}) , validators=[MaxLengthValidator(11),MinLengthValidator(11)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control' ,  'placeholder': 'Enter your phone number'}),
                            validators=[MaxLengthValidator(11), MinLengthValidator(11)],)

class RegisterSecondForm(forms.Form):
    code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter your Code'}),)