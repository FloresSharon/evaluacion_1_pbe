from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request,'home.html')

def mostrar_servicio(request):
    datos = {
        "nombre1": "Lavado de vehículos",
        "valor": 10000,
        "nombre2": "Aspiración",
        "valor2": 5000,
        "nombre3": "Inflar llantas",
        "valor3": 2500,
        "nombre4": "Llenar tanque",
        "valor4": 50000
    }
    return render(request,'servicio.html', datos)