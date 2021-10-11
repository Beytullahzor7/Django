from django.db import models

# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=100) #inputText
    description = models.TextField() #textArea
    image = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image



