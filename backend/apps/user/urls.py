from django.urls import path

from .views import (
    ActivateDeactivateUser,
    AddAvatarView,
    UserCreateView,
    UserDeleteView,
    UserDepriveAdminView,
    UserListView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/make_admin', UserToAdminView.as_view(), name='user_make_admin'),
    path('<int:pk>/deprive_admin', UserDepriveAdminView.as_view(), name='user_deprive_admin'),
    path('<int:pk>/activate_deactivate', ActivateDeactivateUser.as_view(), name='user_activate_deactivate'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
    path('list', UserListView.as_view(), name='user_list'),
    path('avatar', AddAvatarView.as_view(), name='user_add_avatar'),
]