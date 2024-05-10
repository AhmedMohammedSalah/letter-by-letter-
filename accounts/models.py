from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from django.core.validators import RegexValidator

    
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "users/%s/%s.%s" % (instance.fname, instance.fname, extension)
class CustomUser(AbstractUser):
    nid_validator = RegexValidator(regex=r'^\d{14}$', message="الرقم القومي لابد ان يكون 14 رقم ")
    nid = models.CharField(max_length=14, unique=True, validators=[nid_validator])
    fname=models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='customuser_set')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)
    def __str__(self):
        return self.fname
    
    
    
    
    
    
