from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='main_dashboard'),
    path('data', views.dashboard_data, name='dashboard_data'),
]
