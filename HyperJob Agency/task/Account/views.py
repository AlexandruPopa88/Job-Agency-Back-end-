from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.
class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'account/signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'account/login.html'
