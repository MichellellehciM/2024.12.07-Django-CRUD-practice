from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm

# Create your views here.


def home(request):
    if request.POST:
        form = ResumeForm(request.POST)
        form.save()
        return redirect("resumes:home")
    resumes = Resume.objects.all()
    return render(request, "resumes/home.html", {"resumes": resumes})


def new(request):
    resume = Resume()
    form = ResumeForm(instance=resume)
    return render(request, "resumes/new.html", {"form": form})


def show(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:
        form = ResumeForm(request.POST, instance=resume)
        form.save()
        return redirect("resumes:home")
    return render(request, "resumes/show.html", {"resume": resume})


def edit(request, id):
    resume = get_object_or_404(Resume, id=id)
    form = ResumeForm(instance=resume)
    return render(request, "resumes/edit.html", {"resume": resume, "form": form})


def delete(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:
        resume.delete()
        return redirect("resumes:home")
    return render(request, "resumes/delete.html")
