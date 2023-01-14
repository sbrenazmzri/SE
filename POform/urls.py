from django.urls import path
from . import views

urlpatterns = [
    path('POform/purchase_order/', views.purchase_order, name='purchase-order'),
    path('purchase_order/success/', views.purchase_order_success, name='success'),
]