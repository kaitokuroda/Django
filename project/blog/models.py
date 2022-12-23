#データベースとのやりとり

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    #slug 投稿番号
    slug = models.SlugField()
    #本文
    intro = models.TextField()
    body = models.TextField()
    #投稿した日時
    posted_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)