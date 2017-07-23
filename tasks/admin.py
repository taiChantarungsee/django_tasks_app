from django.contrib import admin
from .models import Task, User

myModels = [Task]
admin.site.register(myModels)
