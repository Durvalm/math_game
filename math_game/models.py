from django.db import models

# Create your models here.


class Math(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    points = models.IntegerField()
    session_key = models.CharField(max_length=100)
    rounds = models.IntegerField()

    def answer(self):
        return self.x * self.y
