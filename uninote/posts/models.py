from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta():
        ordering = ['-created_at']
        #unique_together = ['user','message']

class Comment(models.Model):
    post = models.ForeignKey('posts.Post',related_name="comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,related_name='usercomments',on_delete=models.CASCADE)
    message = models.TextField()
    username=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.post.user.username,'pk':self.pk})

    class Meta():
        ordering = ['-created_at']
