from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.http.response import Http404
# Create your views here.

def boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
