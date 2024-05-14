from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser
def vid_upload(instance, filename):
    vid_name, extension = filename.split(".")
    return "lessons/%s/%s.%s" % (vid_name, vid_name, extension)

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.FileField(upload_to=vid_upload, blank=True, null=True)

    lesson_type = models.CharField(choices=[('reading', 'قراءة'), ('listening', 'استماع'), ('writing', 'كتابة')], max_length=20)
    completed_by_users = models.ManyToManyField(CustomUser, through='UserLessonCompletion')

    def __str__(self):
        return self.title
    
class UserLessonCompletion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
