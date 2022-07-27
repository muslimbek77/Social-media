from django.contrib import admin

from message.models import Chat,Message,Comment

# Register your models here.
admin.site.register(Chat)
admin.site.register(Comment)
admin.site.register(Message)