from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Projects here")

def project(request, pk):
    return HttpResponse(f"Project details code nro: {str(pk)}")
