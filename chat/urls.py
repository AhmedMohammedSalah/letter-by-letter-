# في ملف urls.py

from django.urls import path
from . import views
app_name='chat'

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
    path('send/', views.send_message, name='send_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('fetch_messages/', views.fetch_messages, name='fetch_messages'),


]
