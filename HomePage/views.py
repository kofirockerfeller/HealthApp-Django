from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "HomePage/index.html")

def bmi(request):
    return HttpResponse("These are your current suggested foods")

def records(request):
    return HttpResponse("Here are your current health records")

def greet(request, name):
    return render(request, "HomePage/greet.html", {
        "name": name.capitalize()
    })