from django.db import models
from datetime import datetime
from django_resized import ResizedImageField
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
import os
import datetime


def get_image_path(instance, filename):
    now = datetime.datetime.now()
    year = str(now.year)
    month = now.strftime("%b")
    day = str(now.day)
    filename = day+month+year
    image_dir = os.path.join('fulls', year)
    return os.path.join(image_dir, filename+".JPG")


def get_thumbnail_path(instance, filename):
    now = datetime.datetime.now()
    year = str(now.year)
    month = now.strftime("%b")
    day = str(now.day)
    filename = day+month+year
    image_dir = os.path.join('thumbs', year)
    return os.path.join(image_dir, filename+".JPG")


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    post_image_full = ResizedImageField(upload_to=get_image_path, blank=False, null=True, force_format='JPEG')
    post_image_thumb = ResizedImageField(size=[500, 600], crop=['middle', 'center'], upload_to=get_thumbnail_path, blank=False, null=True, force_format='JPEG')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
