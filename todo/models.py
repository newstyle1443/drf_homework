from django.db import models
from users.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    completion_at = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    