from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from .models import Order
from .forms import OrderForm

def dashboard(request):
    total_orders = Order.objects.count()
    revenue = Order.objects.aggregate(Sum('total_bill'))['total_bill__sum'] or 0
    status_data = Order.objects.values('status').annotate(count=Count('id'))
    return render(request,'orders/dashboard.html',locals())


def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders_list')
    return render(request,'orders/create_order.html',{'form':form})


def orders_list(request):
    qs = Order.objects.all().order_by('-id')
    status = request.GET.get('status')
    q = request.GET.get('q')
    if status:
        qs = qs.filter(status=status)
    if q:
        qs = qs.filter(customer_name__icontains=q) | qs.filter(phone__icontains=q)
    return render(request,'orders/orders_list.html',{'orders':qs})

def home(request):
    return render(request, 'orders/dashboard.html') 