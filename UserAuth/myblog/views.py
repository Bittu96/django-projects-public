from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(requests):
	return render(requests, 'index.html')

def add(requests):
	val1 = requests.POST['num1']
	val2 = requests.POST['num2']
	sum_ = int(val1) + int(val2)
	return render(requests, 'calc.html',{'result': sum_})

def calc(requests):
    return render(requests, 'calc.html')

def about(requests):
	dests = Destination.objects.all()
	return render(requests, 'about.html',{'dests': dests})