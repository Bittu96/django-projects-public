from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requests):
	return render(requests, 'home.html', {'name':'bittu!'})

def add(requests):
	val1 = requests.POST['num1']
	val2 = requests.POST['num2']
	sum_ = int(val1) + int(val2)
	return render(requests, 'result.html',{'result': sum_})
