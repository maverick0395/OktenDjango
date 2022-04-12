from django.db import models


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'autoparks'
        verbose_name = 'Autopark'

    name = models.CharField(max_length=30)


