from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    picture = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __str__(self):
        return self.name