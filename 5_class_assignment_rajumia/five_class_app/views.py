from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("<h1>My name is Raju Mia.</h1>")

