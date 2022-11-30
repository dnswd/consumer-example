from django.contrib import admin
from user.models import Message, User
# Register your models here.
admin.site.register(User)
admin.site.register(Message)
