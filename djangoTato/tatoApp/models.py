from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    content = models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    