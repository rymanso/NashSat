from django.db import models
from datetime import datetime
import os
import datetime


def get_image_path(instance, filename):
    now = datetime.datetime.now()
    year = str(now.year)
    month = now.strftime("%b")
    day = str(now.day)
    filename = day+month+year
    image_dir = os.path.join('posts', 'templates', 'posts', 'images', year)
    while filename+".png" in image_dir:
        count = 2
        filename = filename + "(" + str(count) + ")"
        count += 1
    return os.path.join(image_dir, filename+".png")


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    post_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


