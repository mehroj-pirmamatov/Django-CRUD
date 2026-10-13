from django.urls import path
from .views import index, create, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('add/', create, name='create'),
    path('edit/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]