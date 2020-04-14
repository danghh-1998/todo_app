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


def update_todo(todo, data):
    if not any(data.values()):
        raise ValidationError
    todo.content = data.get('content') or todo.content
    todo.is_complete = data.get('is_complete') or todo.is_complete
    todo.save(update_fields=['content', 'is_complete'])
    return todo


def delete_todo(todo):
    todo.delete()
