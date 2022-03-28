from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.profile.serializers import AvatarSerializer

from .permissions import IsStaff, IsSuperUser
from .serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return super().get_permissions()


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            raise ValueError('User is already admin')
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class UserDepriveAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            raise ValueError("This user doesn't have Admin rights")
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class ActivateDeactivateUser(GenericAPIView):
    permission_classes = (IsStaff,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserDeleteView(GenericAPIView):
    permission_classes = (IsStaff,)
    queryset = UserModel.objects.all()

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        item = get_object_or_404(UserModel, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        current_user_pk = self.request.user.pk
        print(current_user_pk)
        user_list = UserModel.objects.exclude(pk=current_user_pk)
        return user_list


class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer

    def get_object(self):
        return self.request.user.profile





