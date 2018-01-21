from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import boards
from boards.models import Board
from boards.views import board_topics
# Create your tests here.


class BoardsTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('boards')
        self.response = self.client.get(url)
    
    def test_boards_view_status_code(self):
        url = reverse('boards')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_home_url_resolves_home_view(self):
        view = resolve('/boards/')
        self.assertEquals(view.func, boards)
        
    def testBoardsViewContainsLinkToTopics(self):
        boardTopicsUrl = reverse('board_topics', kwargs = {'pk' : 1})
        self.assertContains(self.response, 'href="{0}"'.format(boardTopicsUrl))
        
        
        
class TopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        board = Board(name = 'Django1', description='Django board1.')
        board.save()
    
    def testBoardTopicsSuccess(self):
        url = reverse('board_topics', kwargs = {'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def testBoardTopicsNotFound(self):
        url = reverse('board_topics', kwargs = {'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
        
    def testBoardTopicsUrlResolvesView(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
        
    def testBoardTopicsContainsBoardsUrl(self):
        url = reverse('board_topics', kwargs = {'pk': 1})
        response = self.client.get(url)
        boardsUrl = reverse('boards')
        self.assertContains(response, 'href="{0}"'.format(boardsUrl))