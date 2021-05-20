from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Resume
from .forms import ResumeForm

class ResumeView(View):
    def get(self, request):
        context = {"resumes": Resume.objects.all}
        return render(request, "resume/ResumeMain.html", context=context)

class ResumeCreate(View):
    def get(self, request):
        if request.user.is_authenticated == True:
            if not request.user.is_staff == True:
                form = ResumeForm()
                return render(request, "resume/ResumeNew.html", {"resume_form": form})
        else:
            return HttpResponse(status=403)

    def post(self, request):
        if request.user.is_authenticated == True:
            if not request.user.is_staff == True:
                form = ResumeForm(request.POST)
                if form.is_valid():
                    NewResume = Resume(description=form.cleaned_data["description"], author=request.user)
                    NewResume.save()
                    return redirect("../home/")
        else:
            return HttpResponse(status=403)