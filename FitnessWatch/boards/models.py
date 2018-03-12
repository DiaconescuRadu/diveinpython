from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name='+')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stravaAuthKey = models.TextField(max_length=4000, null=True)
    stravaUserName = models.TextField(max_length=4000, null=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
