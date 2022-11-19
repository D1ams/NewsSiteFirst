from django.db import models
from django.contrib.auth.models import User

from NewsPortal.resources import POSITIONS, news


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    @staticmethod
    def update_rating(self):
        postrating = 0
        commentrating = 0
        postcommentrating = 0
        for num in self.post_set.all():
            postrating += (num.post_rating*3)
        for num in self.user.comment_set.all():
            commentrating += num.rating
        for i in self.post_set.all():
            for j in i.comment_set.all():
                postcommentrating += j.rating
        self.rating = postcommentrating + postrating + commentrating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=POSITIONS, default=news)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return self.content[:124] + '...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
