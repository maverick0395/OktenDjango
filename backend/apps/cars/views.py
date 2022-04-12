from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer
from pagination.default_pagination import DefaultPagination


class CarListCreateView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CarSerializer
    pagination_class = DefaultPagination
    filterset_class = CarFilter
    queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        return qs


class CarReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


