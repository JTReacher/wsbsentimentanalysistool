from django.shortcuts import render
from django.http import JsonResponse
from main_dashboard.models import Order
from django.core import serializers

# Create your views here.

def dashboard(request):
    return render(request, 'main_dashboard.html', {})


def dashboard_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
