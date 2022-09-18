from django.urls import path,include
from Users.views import dashboard

urlpatterns = [
    path('dashboard/',dashboard,name ='dashboard'),
    ]