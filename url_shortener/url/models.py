from django.db import models


# Create your models here.
class URL(models.Model):
    user_url = models.URLField(max_length=2000)
    shortened_url = models.URLField()
    user_email = models.EmailField()

