from django.urls import path,include
from Users.views import dashboard

urlpatterns = [
    path('', include('allauth.urls')),
    path('dashboard/',dashboard,name ='dashboard'),
    ]