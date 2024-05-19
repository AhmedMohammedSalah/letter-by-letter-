from django.shortcuts import render, redirect
from .models import WordImagePair

def game_view(request):
    pairs = WordImagePair.objects.all()
    context = {'pairs': pairs}
    return render(request, 'game.html', context)

