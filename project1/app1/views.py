from django.shortcuts import render
from django.http import HttpResponse


def course(request):
    return HttpResponse("This is course page")


def home(request):
    return HttpResponse("This is Fastapp home page")


# Create your views here.
