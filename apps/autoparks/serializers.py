from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel


class AutoParkSerializer(ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')

    cars = CarSerializer(many=True, read_only=True)