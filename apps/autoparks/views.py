from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkAddCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        autopark = self.get_object()
        serializer.save(autopark=autopark)

class AutoParkDeleteView(DestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer