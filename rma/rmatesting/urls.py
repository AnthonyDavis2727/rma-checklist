from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputForm, name='input_form'),
]
