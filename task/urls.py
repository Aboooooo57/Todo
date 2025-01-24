from django.urls import path, include

from task import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskModelViewSet, basename='tasks')

urlpatterns = router.urls
