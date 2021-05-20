from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class MainPageView(View):
    def get(self, request):
        return render(request, "hyperjob\MainPage.html")

class HomeView(View):
    def get(self, request):
        return render(request, "hyperjob/home.html")