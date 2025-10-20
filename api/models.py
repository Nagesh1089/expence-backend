# from django.db import models

# # Create your models here.
# from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
