from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    xizmatlar = Servise.objects.all()
    loyihalar = Project.objects.all()[:2]
    context = {"projects":loyihalar,
               "services":xizmatlar}
    return render(malumot, 'index.html',context)

def about(malumot):
    return render(malumot, 'about.html')

def blog(malumot):
    return render(malumot, 'blog.html')

def contact(malumot):
    return render(malumot, 'contact.html')

def services(malumot):
    return render(malumot, 'services.html')

def project(malumot):
    return render(malumot, 'project.html')