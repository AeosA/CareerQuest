from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def user_login(request):
    #if the post has been submitted...
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST) #the post information we have recieved will be submitted....

        if form.is_valid():
            #Login here
            login(request, form.get_user())
            return redirect("cq_setupaccount:addskill") #redirect it to the html/url path you want it to go to
    else:
        form = AuthenticationForm()

    return render(request, 'careerquest_login.html', {"form": form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        #replace with the page you want to see when you log out. maybe like the homepage
        return redirect("cq_register:register") #redirect it to the html/url path you want it to go to    
