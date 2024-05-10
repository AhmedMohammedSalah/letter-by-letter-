from django.urls import path
from .views import writing_lessons,listening_lessons,reading_lessons,lesson_detail
app_name='lessons'
urlpatterns = [
    path('writting/', writing_lessons, name='writting'),
    path('listening/', listening_lessons, name='listening'),
    path('reading/', reading_lessons, name='reading'), 
    path('lessondetail/', lesson_detail, name='reading'), 
]