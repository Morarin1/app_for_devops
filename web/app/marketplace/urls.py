from django.urls import path

from .views import PostViewSet

urlpatterns = [
    path('api/posts/', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('api/posts/<str:pk>', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]
