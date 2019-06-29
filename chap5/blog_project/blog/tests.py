# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user (
            username = 'testuser',
            email = 'test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body = 'Nice body content',
            author = self.user,
        )

    def test_string_representation(self):
        post=Post(title='A sample title')
        self.assertEqual(str(post),post.title)

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'home.html')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'post_detail.html')

# Create your tests here.
