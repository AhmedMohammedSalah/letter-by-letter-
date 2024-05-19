from django.db import models

# Create your models here..
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "games/%s/%s.%s" % (instance.word, image_name, extension)
class WordImagePair(models.Model):
    word = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.word