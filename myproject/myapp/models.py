from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)  # The title of the todo item
    description = models.TextField(blank=True, null=True)  # A more detailed description (optional)
    due_date = models.DateField(blank=True, null=True,default=True)  # The due date for the todo item (optional)

    def __str__(self):
        return self.title