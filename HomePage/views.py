from logging import PlaceHolder
from django import forms
from locale import currency
from django.shortcuts import render
from django.http import HttpResponse

Age= 0
Weight = 0
Height = 0
class NewTaskForm(forms.Form):
    CHOICES = [("Vegan","Vegan"), ("Non-Vegan","Non-Vegan")]
    Age = forms.IntegerField(label="Age", min_value=0, max_value=130, widget=forms.TextInput(attrs={'class': 'intfield', 'placeholder':"Enter your age"}))
    Height = forms.IntegerField(label="Height(cm)", min_value=0, widget=forms.TextInput(attrs={'class': 'intfield', 'placeholder':"Enter your height"}))
    Weight = forms.IntegerField(label="Weight(kg)", min_value=0, widget=forms.TextInput(attrs={'class': 'intfield', 'placeholder':"Enter your weight", 'id': 'weight'}))
    Diet_Status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
def index(request):
    return render(request, "HomePage/index.html")

def bmi(request):
    return render(request, "HomePage/inputhealth.html", {
        "form": NewTaskForm()
    })

def records(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            Age = form.cleaned_data["Age"]
            Height = form.cleaned_data["Height"]
            Weight = form.cleaned_data["Weight"]
        else:
            return render(request, "HomePage/inputhealth.html",{
                "form": form
            })
    bmi = Weight / (Height*Height)
    return render(request, "HomePage/greet.html", {
        "Underweight": bmi < 18.5,
        "Healthy": bmi > 18.5 and bmi < 24.5,
        "Overweight": bmi > 25 and bmi < 29.9,
        "Obese": bmi > 30 and bmi < 39.9
        
        }
    )

def greet(request, name):
    return render(request, "HomePage/greet.html", {
        "name": name.capitalize()
    })

