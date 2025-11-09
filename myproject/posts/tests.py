from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="secret")
        Post.objects.create(title="Test Post", body="This is a test post.", author=user)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.body, "This is a test post.")
        self.assertEqual(post.author.username, "testuser")