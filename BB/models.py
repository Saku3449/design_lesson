from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title