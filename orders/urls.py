from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_order, name='create_order'),
    path('orders/', views.orders_list, name='orders_list'),
]