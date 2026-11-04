from django.db import models

# Create your models here.
class todo_table(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Done = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)