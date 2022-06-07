from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='Koffee')
        self.profile = Profile.objects.create(user = self.user,bio = 'Best female mcee')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('Koffee')
        self.assertTrue(len(profile) > 0)

class PostTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='Koffee')
        self.profile = Profile.objects.create(user = self.user,bio = 'Best female mcee')

        self.post = Post.objects.create(profile = self.profile,caption ='Best female mcee',likes = 0, posted_at='7-06-2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_get_posts(self):
        self.post.save()
        post = Post.get_posts()
        self.assertTrue(len(post) == 1)

class CommentTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='Koffee')

        self.comment= Comment.objects.create(poster= self.user, comment='Best female mcee' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)
