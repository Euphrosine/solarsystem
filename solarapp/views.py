from django.shortcuts import render
from .models import SolarData
from django.http import JsonResponse
from django.utils import timezone

def api_view(request): 
    fixed = request.GET.get('fixed', None)
    tracking = request.GET.get('tracking', None)


    # Create a dictionary to store the data you want to save
    data_to_save = {
        'datetime': timezone.now(),
        'fixed': fixed,
        'tracking': tracking,

    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    SolarData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})


def display_view(request):
    solar_data = SolarData.objects.all()

    # Create a dictionary to store the data with boolean values represented as "ON" or "OFF"
    formatted_data = []

    for data in solar_data:
        formatted_data.append({
            'datetime': data.datetime,
            'fixed': data.fixed,
            'tracking': data.tracking,

        })

    return render(request, 'solarapp/dashboard_view.html', {'solar_data': formatted_data})