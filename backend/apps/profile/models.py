from django.contrib.auth import get_user_model

from django.core.validators import RegexValidator

from django.db import models

from utils.avatar_utils import AvatarUtils


UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()
    phone = models.CharField(max_length=13, validators=(
        RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number. Number must begin with +380 plus 9 digits'),
    ))
    avatar = models.ImageField(upload_to=AvatarUtils.upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')