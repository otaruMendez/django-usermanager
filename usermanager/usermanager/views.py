from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django import forms
from .models import Person

def add(request):
   today = "Hello World"
   feedback = {}
   feedback["name"] = ""
   feedback["email"] = ""
   if (request.method == "POST"):
        name = request.POST.get("fullname", "")
        email = request.POST.get("email", "")
        feedback['name'] = name
        feedback['email'] = email
        try:
            validate_email(email)
            if (len(name) == 0):
                messages.add_message(request, messages.ERROR, 'Name cannot be empty')
            elif (Person.objects.filter(email=email).count() > 0):
                messages.add_message(request, messages.ERROR, 'Email already exists')  
            else:
                messages.add_message(request, messages.SUCCESS, 'Your data was successfully saved')
                Person.objects.create(name=name, email=email)
                feedback['name'] = ""
                feedback["email"] = ""
        except forms.ValidationError:
            messages.add_message(request, messages.ERROR, 'Wrong Email Format')
   return render(request, "add.html", {"feedback" : feedback})

def list(request):
    persons = Person.objects.all()
    return render(request, "view.html", {"persons" : persons})

def home(request):
    return render(request, "home.html")