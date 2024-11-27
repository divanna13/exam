from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', views.task_list, name='task-list'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
