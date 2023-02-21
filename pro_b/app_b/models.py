from django.db import models

class samplemodel(models.Model):
    name = models.CharField(max_length=30)
    sam_id = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.name
