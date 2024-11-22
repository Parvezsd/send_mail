from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
# Create your models here.
class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()
    def __str__(self):
        return str(self.username)
