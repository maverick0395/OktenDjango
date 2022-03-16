from django.db import models

# Create your models here.
class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
        verbose_name = 'Computer'

    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    ram = models.IntegerField()
    screen = models.FloatField()

    def __str__(self):
        return f'{self.brand} {self.model}'

