from django.views import View
from .models import Scooter
from django.http import HttpResponse
import json
from django.core import serializers


class ScooterList(View):
    def get(self, request):
        scooters = Scooter.objects.all()
        data = serializers.serialize('json', scooters)
        return HttpResponse(data)

    def post(self, request, *args, **kwargs):
        scooter_data = json.loads(request.body)

        new_scooter = Scooter(
            status=scooter_data['status'],
            current_speed=scooter_data['current_speed'],
            current_battery=scooter_data.get('current_battery', None)
        )
        new_scooter.save()
        data = serializers.serialize('json', [new_scooter])

        return HttpResponse(data)


class ScooterOperations(View):
    def patch(self, request, *args, **kwargs):
        update_data = json.loads(request.body)
        Scooter.objects.filter(pk=kwargs['id']).update(**update_data)

        return HttpResponse('ok')

    def delete(self, request, *args, **kwargs):
        Scooter.objects.filter(pk=kwargs['id']).delete()

        return HttpResponse('ok')