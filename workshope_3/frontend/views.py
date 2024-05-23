from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_event_form(request):
    return render(request, 'add_event_form.html')

def add_event_form(request):
    return render(request, 'add_event_form.html')

def engines(request):
    engines_list = [
        {
            "name": "",
            "tipo de motor" : "",
            "peso": "",
            "potencia": ""
        }
    ]
    return render(request, 'engines.html', {"Motores": engines_list})

def vehicles(request):
    vehicles_list = [
        {
            "name": "",
            "year" : "",
            "modelo" : "",
            "chasis": "",
            "motor": ""
        }
    ]
    return render(request, 'vehicles.html', {"vehiculos": vehicles_list})