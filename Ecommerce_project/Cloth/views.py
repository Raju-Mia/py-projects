from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    dic_variable =	{
        "name": "Raju Mia",
        "profession": "Student",
        "age": 23,
        "home": "Dhaka"
        }

    context = {"value": dic_variable}
    return render(request, 'index.html', context)