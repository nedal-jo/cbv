#urls.py in app
from django.urls import path
from .views import PrintersList,PrinterDetails,AddPrinter

urlpatterns = [
    path('printers-list/', PrintersList.as_view(), name='printers-list'),
    path('printer-details/<int:pk>/', PrinterDetails.as_view(), name='printer-details'),
    path('add/', AddPrinter.as_view(), name='printer-add'),
]