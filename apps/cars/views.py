from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    permission_classes = AllowAny
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = CarModel.objects.all()
        price_lt = self.request.query_params.get('price_lt', None)
        year_gt = self.request.query_params.get('year_gt', None)
        autopark = self.request.query_params.get('autopark', None)

        if autopark:
            queryset = queryset.filter(autopark=autopark)

        if price_lt:
            queryset = queryset.filter(price__lt=price_lt)

        if year_gt:
            queryset = queryset.filter(year__gt=year_gt)

        return queryset


class CarReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = AllowAny
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


