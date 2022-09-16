from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet
from django.urls import include, path
from rest_framework.authtoken import views


v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
