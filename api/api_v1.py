from django.urls import include, path

urlpatterns = [
    path('cars/', include('apps.cars.urls')),
    path('autoparks/', include('apps.autoparks.urls')),
    path('users/', include('apps.user.urls')),
    path('authentication/', include('apps.authentication.urls')),
]