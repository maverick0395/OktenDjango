from rest_framework.generics import CreateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
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