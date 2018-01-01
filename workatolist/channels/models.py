from django.db import models
from django.utils.text import slugify


class Channel(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
