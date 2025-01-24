from django_filters.rest_framework import FilterSet
from packaging.utils import _
from rest_framework.filters import SearchFilter

from .models import Task

class TaskFilter(FilterSet):
  class Meta:
    model = Task
    fields = {
      'due_date': ['lte', 'gte'],
      'created_at': ['lte', 'gte'],
    }

class CustomSearchFilter(SearchFilter):
  search_title = _('Search')
  search_description = _('Search Base Title Or description.')
