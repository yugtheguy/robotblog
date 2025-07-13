from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    day_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
