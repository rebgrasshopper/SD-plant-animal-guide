from django.conf import settings
from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    genus = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    status = models.CharField(max_length=25)
    image_whole = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_whole_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    image_leaf = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_leaf_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    image_flower = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_flower_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    image_fruit = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_fruit_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    image_alternate1 = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_alternate1_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    image_alternate2 = models.ImageField(upload_to='static/images/', default=None, blank=True, null=True)
    image_alternate2_title = models.CharField(max_length=400, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    uses = models.TextField(default=None, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name