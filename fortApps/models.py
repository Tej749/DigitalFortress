from django.db import models

# Create your models here.

class DataCentre(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    wt = models.CharField(max_length=10)

    class Meta:
        db_table = 'dataCentre'

    def __str__(self) -> str:
        return self.name



