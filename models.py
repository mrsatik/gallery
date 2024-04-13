from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from django.conf import settings
from PIL import Image


class Gallery(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    code = models.CharField(_('code'), max_length=50, unique=True)
    available = models.BooleanField(_('available'), default=True)

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('list')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ("123", ext)
    return os.path.join('uploads', filename)


class Photo(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    available = models.BooleanField(_('available'), default=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo_img = models.ImageField(upload_to=content_file_name)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo_img.name))
        super(Photo, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo_img.path)
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            ext = self.photo_img.path.split('.')[-1]
            name = self.photo_img.path.split('.')[0]
            img.save(img, format={name: self.photo_img.path.join((name, 'v2')), ext: ext})  # saving image at the same path

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos list')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
