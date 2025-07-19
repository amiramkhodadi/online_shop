from django import forms


class LoginForm(forms.Form):
    phone =forms.CharField(max_length=11 , widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
