from django.db import models

PRINTER_SIZE_CHOICES = [
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
]

PRINTER_STATUS_CHOICES = [
    ('Faulty', 'Faulty'),
    ('Working', 'Working'),
]

LOCATION_CHOICES = [
    ('Al Bidda Tower', 'Al Bidda Tower'),
    ('Al Sadd Club', 'Al Sadd Club'),
    ('Al Duhail Club', 'Al Duhail Club'),
]

class Printer(models.Model):
    printer_type = models.CharField(max_length=6, choices=PRINTER_SIZE_CHOICES, default='Large')
    printer_status = models.CharField(max_length=8, choices=PRINTER_STATUS_CHOICES, default='Working')
    serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='Al Bidda Tower')

    def __str__(self):
        return f"{self.serial_number}: {self.printer_type} at {self.location}"