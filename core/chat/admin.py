from django.contrib import admin
from .models import Inbox
from .models import Message

# Register your models here.
admin.site.register(Inbox)
admin.site.register(Message)