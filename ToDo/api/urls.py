from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute, name="routes"),
    path('todo/', views.todoListPage, name="todo"),
    path('todo/<int:page_id>/category/<int:category_id>/', views.todoCategory, name='singleCategory'),
    path('todo/<int:page_id>/category/', views.todoCategory, name="category"),
    path('todo/<int:page_id>/', views.todoListPage, name="delete"),
    path('categories/order', views.update_order, name='updateOrder'),
    path('todo/<int:page_id>/category/<int:category_id>/todo/', views.todo, name='todo'),
    path('todo/<int:page_id>/category/<int:category_id>/todo/<int:todo_id>/', views.todo, name='todo'),
]