from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    desc = models.CharField(max_length=800)

    def __str__(self):
        return self.name
