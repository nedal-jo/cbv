# Generated by Django 5.1.1 on 2024-09-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('describtion', models.TextField()),
                ('price', models.FloatField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
