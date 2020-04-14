from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE
from users.models import User
from .managers import TodoManager


class Todo(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    content = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.SET_NULL, unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TodoManager()

    class Meta:
        app_label = 'todos'
        db_table = 'todo'

    def __str__(self):
        return self.content
