from django.contrib import admin

# Register your models here.
from .models import UserLessonCompletion,Lesson

admin.site.register(Lesson)
admin.site.register(UserLessonCompletion)

