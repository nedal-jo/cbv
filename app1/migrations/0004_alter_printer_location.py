# Generated by Django 5.1.1 on 2024-09-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_printer_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='location',
            field=models.CharField(choices=[('Al Bidda Tower', 'Al Bidda Tower'), ('Al Sadd Club', 'Al Sadd Club'), ('Al Duhai Club', 'Al Duhail Club')], default='Al Bidda Tower', max_length=20),
        ),
    ]
