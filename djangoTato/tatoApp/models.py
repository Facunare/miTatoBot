from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import BooleanField

# Create your models here.

class Messages(models.Model):
    content = models.TextField(max_length=180)
    response = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    