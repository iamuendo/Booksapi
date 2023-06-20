from django.db import models

# Create a class that inherits Models
class Book(models.Model):
    title = models.CharField(max_length=250)
    ISBN = models.CharField(max_length= 17)
    author_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title + ' by ' + self.author_name