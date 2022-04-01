from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('activate/<str:token>', ActivateUserView.as_view(), name='activate_user')
]
