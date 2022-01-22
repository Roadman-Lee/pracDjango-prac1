from django.shortcuts import render, HttpResponse
import random

def index(request):
    return HttpResponse('<h1>Random</h1>'+str(random.random()))

def create(request):
    return HttpResponse('create')

def read(request, id):
    return HttpResponse('read!'+id)
    