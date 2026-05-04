from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum, Count, Q
from .models import Order
from .forms import OrderForm


def dashboard(request):
    totals = Order.objects.aggregate(
        total_orders=Count('id'),
        revenue=Sum('total_bill'),
    )
    status_data = list(Order.objects.values('status').annotate(count=Count('id')))
    pending_orders = sum(s['count'] for s in status_data if s['status'] != 'DELIVERED')
    recent_orders = Order.objects.all()[:5]

    context = {
        'total_orders': totals['total_orders'] or 0,
        'revenue': totals['revenue'] or 0,
        'pending_orders': pending_orders,
        'status_data': status_data,
        'recent_orders': recent_orders,
    }
    return render(request, 'orders/dashboard.html', context)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, f'Order {order.order_id} created successfully!')
            return redirect('orders_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})


def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order {order.order_id} updated successfully!')
            return redirect('orders_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/update_order.html', {'form': form, 'order': order})


def orders_list(request):
    qs = Order.objects.all()

    status = request.GET.get('status', '')
    q = request.GET.get('q', '').strip()

    if status:
        qs = qs.filter(status=status)

    if q:
        qs = qs.filter(
            Q(customer_name__icontains=q) |
            Q(phone__icontains=q) |
            Q(order_id__icontains=q)
        )

    paginator = Paginator(qs, 25)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'orders': page_obj,
        'page_obj': page_obj,
        'paginator': paginator,
        'total_count': paginator.count,
        'status_choices': Order.STATUS_CHOICES,
        'current_status': status,
        'search_query': q,
    }
    return render(request, 'orders/orders_list.html', context)
