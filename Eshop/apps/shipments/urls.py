from django.urls import path
from . import views

urlpatterns = [
    path('',views.ShipmentList.as_view(), name = 'shipment_list'),
    path('<int:shipment_id>/', views.ShipmentDetails.as_view(), name='detail'),
]
