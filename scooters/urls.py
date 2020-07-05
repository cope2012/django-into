from django.urls import path
from .views import ScooterList, ScooterOperations
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', csrf_exempt(ScooterList.as_view())),
    path('<int:id>', csrf_exempt(ScooterOperations.as_view())),
]