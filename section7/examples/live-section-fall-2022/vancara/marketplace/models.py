from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='vehicles')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='vehicles')
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


