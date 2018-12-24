from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class URL(models.Model):
    user_url = models.TextField(validators=[URLValidator()])
    user_email = models.EmailField(blank=True)

