from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Vacancy
from .forms import VacancyForm
from django.contrib.auth.models import User

# Create your views here.
class VacancyView(View):
    def get(self, request):
        context = {"vacancies": Vacancy.objects.all}
        return render(request, "vacancy/VacancyMain.html", context=context)

class VacancyCreate(View):
    def get(self, request):
        if request.user.is_authenticated:
            if User.is_staff:
                form = VacancyForm()
                return render(request, "vacancy/VacancyNew.html", {"vacancy_form": form, "user": User})
        return HttpResponse(status=403)

    def post(self, request):
        if request.user.is_authenticated == True:
            if User.is_staff == True:
                form = VacancyForm(request.POST)
                if form.is_valid():
                    NewVacancy = Vacancy(description=form.cleaned_data["description"], author=request.user)
                    NewVacancy.save()
                    return redirect("../home/")
        return HttpResponse(status=403)