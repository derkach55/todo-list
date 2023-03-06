from django.urls import path

from todo_list.views import (
    TaskListView,
    ChangeStatus,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/change_status/', ChangeStatus.as_view(), name='change-status'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]

app_name = 'todo_list'
