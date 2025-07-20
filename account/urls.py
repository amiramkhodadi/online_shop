from django.urls import path
from . import  views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register2/', views.RegisterSecoundStepView.as_view(), name='register2')
  ]