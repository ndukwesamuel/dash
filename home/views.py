from django.shortcuts import render,redirect
from django.http import HttpResponse

from home.models import *
from home.forms import OrderForm


# Create your views here.




def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    out_of_delivered = orders.filter(status='out for delivery').count()
    pending = orders.filter(status='pending').count()

    context = {'total_customers':total_customers,
        'orders':orders,'total_orders':total_orders, 'customers':customers, 'pending':pending, 'delivered':delivered, 'out_of_delivered':out_of_delivered}

    return render(request, 'dashboard.html', context)


def product(request):
    products = Product.objects.all()

    context = {"products":products,}

    return render(request, 'product.html', context)

def customer(request,id_test):
    customer = Customer.objects.get(id=id_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders,'order_count':order_count}

    return render(request, 'customer.html',context)

def create_ord(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:

        bad = form.errors
        print(bad)
        context = {'bad': bad}

    context = {'form':form}



    return render(request, 'create_order.html', context)

def update_ord(request,id_test):
    order = Order.objects.get(id=id_test)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form =OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        bad = form.errors
        print(bad)
        context = {'bad': bad}

    context = {'form': form}
    
    return render(request, 'create_order.html', context)
    


def delete_form(request,id_test):
    order = Order.objects.get(id=id_test)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'item':order}
    return render(request, 'delete.html', context)