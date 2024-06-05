from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=500)
    food_description = models.TextField()
    food_image = models.ImageField(upload_to="foodimages")
    
