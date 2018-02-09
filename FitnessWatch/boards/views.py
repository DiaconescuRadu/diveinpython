from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board
from django.http.response import Http404
from django.contrib.auth.models import User
from boards.models import Topic, Post
# Create your views here.

def boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk = pk)
    
    topics = board.topics.all()
    return render(request, 'topics.html', {'board': board, 'topics': topics})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk = pk)
    
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
