from django.contrib import admin
from .models import Task, User

myModels = [Task, User]
admin.site.register(myModels)