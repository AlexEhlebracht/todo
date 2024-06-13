from django.contrib import admin
from .models import TodoPage, TodoCategory, Todo

# Register your models here.
admin.site.register(TodoPage)

admin.site.register(TodoCategory)

admin.site.register(Todo)