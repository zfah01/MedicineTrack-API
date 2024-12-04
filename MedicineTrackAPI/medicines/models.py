from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    expiration_date = models.DateField()
    batch_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

