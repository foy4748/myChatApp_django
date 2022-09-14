from django.contrib import admin

# Register your models here.

from .models import MessageThread, Message, Participant

admin.site.register(MessageThread)
admin.site.register(Message)
admin.site.register(Participant)
