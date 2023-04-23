from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.urls import reverse

User = get_user_model()

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})




class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})
