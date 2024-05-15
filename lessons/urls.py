from django.urls import path
from .views import writing_lessons,listening_lessons,reading_lessons,lesson_detail,mark_lesson_completed
app_name='lessons'
urlpatterns = [
    path('writting/', writing_lessons, name='writting'),
    path('listening/', listening_lessons, name='listening'),
    path('reading/', reading_lessons, name='reading'), 
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'), 
    path('lesson/<int:lesson_id>/mark_completed/', mark_lesson_completed, name='mark_completed'),  


]