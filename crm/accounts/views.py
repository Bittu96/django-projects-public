from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    total_pending = orders.filter(
        status='pending').count()
    total_delivered = orders.filter(
        status='delivered').count()
    print(total_pending, total_delivered)

    context = {'customers': customers,
               'orders': orders,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'pending': total_pending,
               'delivered': total_delivered
               }

    return render(request, 'dashboard.html', {'context': context})


def customers(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer,
               'orders': orders,
               'total_orders': total_orders,
               'myFilter': myFilter,
               }

    return render(request, 'customers.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_order(request):
    form = OrderForm()

    if request.method == 'POST':
        print(f'printing post rewuest {request.POST}')
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        print(f'printing post rewuest {request.POST}')
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'delete.html', context)
