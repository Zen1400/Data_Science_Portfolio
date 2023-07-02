from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name






class Room(models.Model) :
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # Many to Many relation, I've to specify related_name because I used User as a host
    #  blank = True to enable submiting a form
    participants = models.ManyToManyField(User, related_name='Participant', blank=True)
    description = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)   # auto_now   updates the field every time save method called
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add  sets timezone only when created
    class Meta :
        ordering = ['-updated', '-created']       # will show elements based on order and the - for descending order

    # Create a string representation of the room
    def __str__(self) -> str:
        return self.name



class Message(models.Model):
    # Here the user model is imported because a built in model exists
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # CASCADE will delete message if the room is deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)   # auto_now   updates the field every time save method called
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add  sets timezone only when created

    # This makes sure they are ordered when showed
    class Meta :
        ordering = ['-updated', '-created']
    # Create a string representation of the message that will show when you refer to it
    # To show the whole message use message.body
    def __str__(self) -> str:
        return self.body[:50]
