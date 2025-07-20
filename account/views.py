from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils import timezone
from .models import User
import random

from account.forms import LoginForm, RegisterForm, RegisterSecondForm
from account.models import VerificationCode


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

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request , 'account/register.html' , {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['phone']
            code = random.randint(111111, 999999)
            VerificationCode.objects.create(phone=cd , code = code)
            return redirect(reverse('register2') + f'?phone={cd}&code={code}')
        else :
            form.add_error("phone","Your Phone Number isn't valid")

        return render(request , 'account/register.html' , {'form':form})


class RegisterSecoundStepView(View):

    def get(self, request):
        right_code = request.GET.get('code')
        form = RegisterSecondForm()
        return render(request , 'account/register_step_2.html' , {'form':form , 'right_code':right_code})

    def post(self, request):
        phone = request.GET.get('phone')
        right_code = request.GET.get('code')
        form = RegisterSecondForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                code_obj = VerificationCode.objects.get(phone=phone, code=code)

                if code_obj.is_valid():
                    user , is_create  = User.objects.get_or_create(phone=phone)
                    login(request, user)
                    # chon darim expired shdn ono ham beresi mikonim v error tolid mikonim pass nbaid in obj ro az data base pak konim
                    # code_obj.delete()
                    return redirect('/')

                else:
                    form.add_error('code', 'code is expired.')

            except VerificationCode.DoesNotExist:
                form.add_error('code', 'Your code is wrong')

        return render(request, 'account/register_step_2.html', { 'form' : form ,'right_code' : right_code })