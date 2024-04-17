from django.shortcuts import render
from .models import Chat
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chats():
    chats = Chat.objects.all()

    return render(request, 'chat/chats.html', {'chats': chats})