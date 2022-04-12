from django.urls import path

from .views import AutoParkAddCarView, AutoParkDeleteView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='autopark_list_create'),
    path('<int:pk>', AutoParkDeleteView.as_view(), name='autopark_delete'),
    path('<int:pk>/add_car/', AutoParkAddCarView.as_view(), name='autopark_add_car')
]