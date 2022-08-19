from django.urls import path,include
from Users.views import user_register_view

urlpatterns = [
    path('', include('allauth.urls')),
    #path('user-register/',user_register_view,name ='user-register'),
    ]