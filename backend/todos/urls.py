from django.urls import path

from .apis import *

urlpatterns = [
    path('todos/create', TodoCreateApi.as_view(), name='todo_create'),
    path('todos', TodoListApi.as_view(), name='todo_list'),
    path('todos/<int:todo_id>/update', TodoUpdateApi.as_view(), name='todo_update'),
    path('todos/<int:todo_id>/delete', TodoDeleteApi.as_view(), name='todo_delete')
]
