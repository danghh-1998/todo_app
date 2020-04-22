from rest_framework.exceptions import APIException, ValidationError

from .models import Todo


def create_todo(data, **kwargs):
    user = kwargs.get('user')
    data['user'] = user
    return Todo.objects.create(**dict(data))


def get_todo_by(**kwargs):
    todo = Todo.objects.filter(**kwargs).first()
    if not todo:
        raise APIException('object not found')
    return todo


def get_completed_todos():
    return list(Todo.objects.filter(is_complete=True))


def update_todo(todo, data):
    if not any(data.values()):
        raise ValidationError
    todo.content = data.get('content')
    todo.is_complete = data.get('is_complete')
    todo.save(update_fields=['content', 'is_complete'])
    return todo


def delete_todo(todo):
    todo.delete()
    return todo


def delete_completed_todos(todos):
    for todo in todos:
        todo.delete()
