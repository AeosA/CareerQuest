from django.urls import path
from . import views

app_name  = "cq_setupaccount"
urlpatterns = [
    path('', views.setupAccount, name = "setup"),
    path('add-skill/', views.ProfileSetup, name = "addskill"),
    #Add path for adding skill
]