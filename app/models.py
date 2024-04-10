from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    geo = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.content
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
