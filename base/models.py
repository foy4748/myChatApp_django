from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MessageThread(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message_thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE)

