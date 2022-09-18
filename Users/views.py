from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Users.forms import user_register_form


'''
comentado
    def user_register_view(request):
    
    if request.method == 'GET':
        form = user_register_form()
        context = {'form': form}
        return render(request,'Users/user_register_template.html',context = context)
'''
@login_required
def dashboard(request):
    user = request.user
    context = {}
    print(user)
    return render (request,'users/dashboard.html',context)

