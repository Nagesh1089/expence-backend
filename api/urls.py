# from django.urls import path
# from .views import TaskListCreate, TaskDetail

# urlpatterns = [
#     path('tasks/', TaskListCreate.as_view(), name='task-list'),
#     path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]
