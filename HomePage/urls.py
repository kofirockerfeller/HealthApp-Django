from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bmi", views.bmi, name="bmi"),
    path("records", views.records, name="records"),
    path("status", views.status, name="status")
]