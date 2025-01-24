from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from task.filters import TaskFilter, CustomSearchFilter
from task.models import Task
from task.serializers import TaskSerializer, UpdateTaskSerializer


class TaskModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return UpdateTaskSerializer
        return TaskSerializer
