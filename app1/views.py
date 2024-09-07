#views.py
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Printer
from django.urls import reverse_lazy
class PrintersList(ListView):
    model = Printer
    template_name ='printers_list.html'
    context_object_name = 'printers'
    paginate_by = 20
    # Override get_queryset to filter by location
    def get_queryset(self):
        queryset = super().get_queryset()
        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(location=location)
        return queryset
        
class PrinterDetails(DetailView):
    model=Printer
    template_name='printer_details.html'
    # pk_url_kwarg='pk'
    
class AddPrinter(CreateView):
    model=Printer
    template_name='add_printer.html'
    fields= ['printer_type','printer_status','serial_number','location']
    success_url=reverse_lazy('printers-list')