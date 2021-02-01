from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def get_name() :
        return self.name
