from django.shortcuts import render

def index(request):
    context = {'Prueba':'Hola Mundo'}
    return render(request,'index.html',context = context)



