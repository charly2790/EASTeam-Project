from django.urls import path
from Users.views import user_register_view

urlpatterns = [path('user-register/',user_register_view,name ='user-register'),]