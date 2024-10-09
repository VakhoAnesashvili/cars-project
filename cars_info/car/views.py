from django.shortcuts import render
from .models import Car
from .forms import CarForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_form.html'
    success_url = reverse_lazy('car-list')

class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_form.html'
    success_url = reverse_lazy('car-list')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car_delete.html'
    success_url = reverse_lazy('car-list')
