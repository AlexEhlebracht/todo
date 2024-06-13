from django.db import models

class TodoPage(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    
class TodoCategory(models.Model):
    name = models.CharField(max_length=16)
    order = models.IntegerField(default=0)
    todo_page = models.ForeignKey(TodoPage, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

class Todo(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(TodoCategory, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title