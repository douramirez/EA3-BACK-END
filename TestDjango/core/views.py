from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home.html')

def test (request):
    return render(request, 'test.html')

def form (request):
    return render(request, 'form_contacto.html')
    


