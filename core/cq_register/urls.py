from django.urls import path

from. import views
app_name="cq_register"

urlpatterns = [
    path('', views.register, name = "register")
]