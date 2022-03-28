# Generated by Django 4.0.3 on 2022-03-27 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\s])[^\\s]{8,20}$', 'Password must contain 1 num, 1 uppercase letter, 1 lowercase letter, 1 non-alpha-numeric')]),
        ),
    ]
