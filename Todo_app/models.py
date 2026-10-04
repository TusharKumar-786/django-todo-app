from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=[('Low','Low'), ('Medium', "Medium"), ("High","High")],
        default='Low'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos"
    )

    def __str__(self):
        return self.title