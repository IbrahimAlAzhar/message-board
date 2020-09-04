from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self): # a string representation of the model
        return self.text[:100]