from django.shortcuts import render, redirect
from .models import Person

def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {'all_person': all_person})


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        Person.objects.create(name=name, age=age)
        return redirect('/')

    return render(request, 'form.html')