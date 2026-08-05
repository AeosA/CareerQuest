from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm


def register(request):
    #if the post has been submitted...
    if request.method == "POST":
        form = RegistrationForm(request.POST) #the post information we have typed/inputted will be submitted....

        if form.is_valid():
            login(request, form.save())
            return redirect("cq_login:login") #redirect it to the html/url path you want it to go to...in this case, lead user to the login page
    else:
        #Prompts user to fill out an empty form to create an account (username, password)
        form = RegistrationForm()

    #render the html page and send the "form" to be accessible in the html template
    return render(request, 'careerquest_register.html', {"form": form})