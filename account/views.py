from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from account.forms import LoginForm


# Create your views here.
# def login(request):
#     return render(request, 'account/login.html'  , {})

class LoginView(View):
    def get(self, request):
        form =LoginForm()
        return render(request , 'account/login.html' , {'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                return redirect('/')

            else :
                form.add_error("phone","you dont have any account ; please register first")
        else :
            form.add_error("phone","invalid data")

        return render(request , 'account/login.html' , {'form':form})
 #