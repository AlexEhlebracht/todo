from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoPage, TodoCategory, Todo
from .serializers import TodoPageSerializer, TodoCategorySerializer, TodoSerializer
import json
from django.http import JsonResponse

@api_view(['GET'])
def getRoute(request):

    routes = [
        {
            'Endpoint': '/todo/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of todo objects'
        },
        {
            'Endpoint': '/todo/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single todo object'
        },
        {
            'Endpoint': '/todo/create',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Creates a new note with data sent in the post request'
        },
        {
            'Endpoint': '/todo/id/update',
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Updates a todo object with data sent in the post request'
        },
        {
            'Endpoint': '/todo/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a todo object'
        }
    ]

    return Response(routes)

@api_view(['GET', 'POST', 'DELETE'])
def todoListPage(request, page_id=None):
    if request.method == 'GET':
        todo_pages = TodoPage.objects.all()
        serializer = TodoPageSerializer(todo_pages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoPageSerializer(data=request.data)
        if serializer.is_valid():
            todo_page = serializer.save()
            TodoCategory.objects.create(name='Todo', todo_page=todo_page, order=0)
            TodoCategory.objects.create(name='Completed', todo_page=todo_page, order=1)
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        todo_page = TodoPage.objects.get(id=page_id)
        todo_page.delete()
        return Response('Todo Page Deleted')

@api_view(['GET', 'POST', 'DELETE'])
def todoCategory(request, page_id, category_id=None):
    if request.method == 'GET':
        todo_page = TodoPage.objects.get(id=page_id)
        categories = todo_page.categories.all()
        serializer = TodoCategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        todo_page = TodoPage.objects.get(id=page_id)
        serializer = TodoCategorySerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.validated_data.get('order', 0)
            serializer.save(todo_page=todo_page, order=order)
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        category = TodoCategory.objects.get(id=category_id)
        category.delete()
        return Response('Category Deleted')
    
@api_view(['POST'])
def update_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        for order, category_id in enumerate(data):
            category = TodoCategory.objects.get(id=category_id)
            category.order = order
            category.save()
            print(order)
            print(category, category.order)
        return JsonResponse({'status': 'success'})
    
@api_view(['GET', 'POST', 'DELETE'])
def todo(request, page_id=None, category_id=None, todo_id=None):
    if request.method == 'GET':
        category = TodoCategory.objects.get(id=category_id)
        todos = category.todos.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        category = TodoCategory.objects.get(id=category_id)
        request.data['category'] = category_id
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        print("hit")
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return Response('Todo Deleted')