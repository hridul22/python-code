from django.db import models

# Create your models here
class Task(models.Model):
    task = models.CharField(max_length=300)
    priority = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return self.task


