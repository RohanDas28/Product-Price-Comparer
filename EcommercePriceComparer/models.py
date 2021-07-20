from django.db import models

# Create your models here.

class Contact(models.Model):
    sr = models.AutoField
    email = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    desc = models.CharField(max_length=800)

    def __str__(self):
        return self.name
