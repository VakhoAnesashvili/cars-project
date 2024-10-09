from django.urls import path
from .views import CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('create/', CarCreateView.as_view(),name='car-create'),
    path('', CarListView.as_view(),name='car-list'),
    path('<int:pk>/', CarDetailView.as_view(),name='car-detail'),
    path('<int:pk>/update/', CarUpdateView.as_view(),name='car-update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(),name='car-delete'),

]