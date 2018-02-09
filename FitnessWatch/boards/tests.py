from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from boards.models import Board, Topic, Post
from boards.views import boards
from boards.views import board_topics
from boards.views import new_topic
from django.contrib.auth.models import User
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
        
    def testBoardTopicsContainsNavigationLinks(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        boards_url = reverse('boards')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(boards_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
        
class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
    
    def testBoardTopicsSuccess(self):
        url = reverse('new_topic', kwargs = {'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def testBoardTopicsNotFound(self):
        url = reverse('new_topic', kwargs = {'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
        
    def testBoardTopicsUrlResolvesView(self):
        view = resolve('/boards/1/new')
        self.assertEquals(view.func, new_topic)
        
    def testBoardTopicsContainsBoardsUrl(self):
        url = reverse('new_topic', kwargs = {'pk': 1})
        response = self.client.get(url)
        boardsUrl = reverse('boards')
        self.assertContains(response, 'href="{0}"'.format(boardsUrl))
        
    def testBoardTopicsContainsParentBoardUrl(self):
        url = reverse('new_topic', kwargs = {'pk': 1})
        response = self.client.get(url)
        boardsUrl = reverse('boards')
        parentBoardUrl = reverse('board_topics', kwargs = {'pk': 1})
        self.assertContains(response, 'href="{0}"'.format(boardsUrl))
        self.assertContains(response, 'href="{0}"'.format(parentBoardUrl))
    
    def test_csrf(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
        