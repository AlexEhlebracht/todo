from rest_framework import serializers
from .models import TodoPage, TodoCategory, Todo

class TodoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoCategory
        fields = ['id', 'name', 'order']

class TodoPageSerializer(serializers.ModelSerializer):
    categories = TodoCategorySerializer(many=True, read_only=True)

    class Meta:
        model = TodoPage
        fields = ['id', 'name', 'categories']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'category']