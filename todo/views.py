from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signupuser(request):
    if request.method == 'GET':
        return render(request, "todo/signupuser.html", {'form':UserCreationForm()})
    else:
        #Create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #Wsto se ocupa de crear el nuevo user object
                user.save() #Esto lo guarda en la base de datos
                login(request, user) #esto lo loguea
                return redirect('currenttodos') #Una vez logueado lo redirigimos a la pagina donde van a estar los todos
            except IntegrityError:
                return render(request, "todo/signupuser.html", {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'}) #Esto maneja el error de que el usuario ya exista
        else:
            return render(request, "todo/signupuser.html", {'form':UserCreationForm(), 'error':'Passwords did not match'}) #esto maneja el error de que la passw1 y la passw2 no coincidan

def currenttodos(request):
    return render(request, "todo/currenttodos.html")
