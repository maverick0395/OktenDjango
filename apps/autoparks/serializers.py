from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')

    cars = CarSerializer(many=True, read_only=True)