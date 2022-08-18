from django.shortcuts import render
from django.contrib.auth.models import User
from Users.forms import user_register_form


def user_register_view(request):
    
    if request.method == 'GET':
        form = user_register_form()
        context = {'form': form}
        return render(request,'Users/user_register_template.html',context = context)

