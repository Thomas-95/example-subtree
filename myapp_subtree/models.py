from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_text = models.TextField()
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.article_title

    def count_article_comments(self):
        return self.comments.count()


class Comment(models.Model):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text

