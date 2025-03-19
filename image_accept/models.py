from django.db import models

# Create your models here.
class image_model(models.Model):
    image = models.ImageField(upload_to='image/')
    updated = models.DateTimeField(auto_now=True, null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)

    class Meta:
        ordering = ['-updated', '-created']