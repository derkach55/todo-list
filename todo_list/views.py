from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class ChangeStatus(generic.View):

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.status = not task.status
        task.save()
        return HttpResponseRedirect(reverse_lazy('todo_list:task-list'))


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo_list:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list:task-list')


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ['content', 'deadline']
    success_url = reverse_lazy('todo_list:task-list')


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo_list:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo_list:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('todo_list:tag-list')
