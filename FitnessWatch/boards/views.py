from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board
from django.http.response import Http404
# Create your views here.

def boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk = pk)
    return render(request, 'topics.html', {'board': board})
