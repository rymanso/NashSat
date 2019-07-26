from django.db import models
from datetime import datetime
from django_resized import ResizedImageField
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
    #created_at = models.DateField(default=datetime.datetime.now, auto_now_add=True)
    post_image_full = ResizedImageField(upload_to=get_image_path, blank=False, null=True, force_format='JPEG')
    post_image_thumb = ResizedImageField(size=[500, 600], crop=['middle', 'center'], upload_to=get_thumbnail_path, blank=False, null=True, force_format='JPEG')
    '''
    NOTE: The following code has been added to django_resized.ResizedImageField.save(): 
    
            if self.field.force_format in ['JPEG', 'JPG', 'jpeg', 'jpg']:
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
    This is to ensure that if the uploaded image is not a JPEG image it gets flattened as needed.
    Ryan Mansoor 
    '''
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
