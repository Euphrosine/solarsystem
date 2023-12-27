from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.api_view, name='api_view'),
    path('', views.display_view, name='display_view'),
]

