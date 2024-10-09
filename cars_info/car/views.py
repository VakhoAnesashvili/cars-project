from django.shortcuts import render
from .models import Car
from .forms import CarForm, CarFilterForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_form.html'
    success_url = reverse_lazy('car-list')

class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(brand__icontains=search_query) | 
                Q(model__icontains=search_query) | 
                Q(model_year__icontains=search_query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = CarFilterForm(self.request.GET)
        return context
    
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
