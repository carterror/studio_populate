from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# # Create your models here.
# class UserProfile(User):
#     bio = models.TextField(blank=True, null=True)    
#     # class Meta(AbstractUser.Meta):
#     #     swappable = "AUTH_USER_MODEL"
        
#     def __str__(self):
#         return self.username