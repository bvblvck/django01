from django.db import models
from django.contrib.auth import get_user_model


class Links(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = get_user_model()
    active = models.BooleanField(default=True)