from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(MPTTModel):
    channel = models.ForeignKey(Channel, related_name='categories')
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='subcategories', db_index=True)

    def save(self, *args, **kwargs):
        slug_name = f'{self.channel.slug} {self.name}'
        if self.parent:
            slug_name = f'{self.parent.slug} {self.name}'
        self.slug = slugify(slug_name)
        super().save(*args, **kwargs)
