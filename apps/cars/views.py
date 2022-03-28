from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        price_lt = self.request.query_params.get('price_lt', None)
        if price_lt:
            qs = qs.filter(price__lt=price_lt)
        return qs


class CarReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


