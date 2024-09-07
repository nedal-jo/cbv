from django.contrib import admin
from .models import Printer
class AdminView(admin.ModelAdmin):
    list_display=['printer_type','serial_number']
# Register your models here.
admin.site.register(Printer,AdminView)