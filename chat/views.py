
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def chat_room(request):
    messages = Message.objects.all()
    return render(request, 'chat_room.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
    return redirect('chat:chat_room')

@login_required
def delete_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        if request.user.is_staff or request.user == message.user:
            message.delete()
    except Message.DoesNotExist:
        pass
    return redirect('chat:chat_room')

def fetch_messages(request):
    messages = Message.objects.all().order_by('timestamp')
    messages_data = [{
        'id': msg.id,
        'user': msg.user.username,
        'fname': msg.user.fname,
        'content': msg.content,
    } for msg in messages]
    return JsonResponse({'messages': messages_data})