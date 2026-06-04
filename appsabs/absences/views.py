from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'home.html')

def bonjour(request):
    nom = request.GET["nom"]
    return render(request, 'appsabs/bonjour.html', {"nom": nom})
