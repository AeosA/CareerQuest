from django.shortcuts import render

def HomeView(request):
    return render(request, 'careerquest_home.html')