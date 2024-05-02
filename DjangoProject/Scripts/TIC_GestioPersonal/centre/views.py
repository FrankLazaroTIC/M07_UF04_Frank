from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import PersonaForm
from .models import UsersTIC

# Create your views here.

def index(request):
    return render(request, 'index.html')

def teachers(request):
    return render(request, 'teachers.html')

def students(request):
        return render(request, 'students.html')
    
def form(request):
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = ({'form': form})
    return render(request, 'form.html',context)

def llistarUsers(request):
    persones = list(UsersTIC.objects.all())
    context = {'persones': persones}
    return render(request, 'students.html', context)
    
def llistarProfessors(request):
    persones = list(UsersTIC.objects.all())
    professors = []
    context = {'professors': professors}
    for p in persones:
        if p.rol == 'Teacher' or p.rol == 'teacher':
            professors.append(p)
    return render(request, 'teachers.html', context)

def updateUser(request, id):
    persona = UsersTIC.objects.get(id=id)
    form = PersonaForm(instance=persona)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'form.html', context)

def llistarUsersIndex(request):
    persones = list(UsersTIC.objects.all())
    students = []
    context = {'students': students}
    for p in persones:
        if p.rol == 'Student' or p.rol == 'student':
            students.append(p)
    return render(request, 'index.html', context)

def deleteUser(request, id):
    persona = UsersTIC.objects.get(id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('/')
    context = {'persona': persona}
    return render(request, 'deleteUser.html', context)