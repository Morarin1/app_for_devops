from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from marketplace.models import Post
from marketplace.serializers import PostSerializer


class PostViewSet(ViewSet):

    def list(self, request):  # /api/posts
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/posts
        pass

    def retrieve(self, request, pk=None):  # /api/posts/<str:id>
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/posts/<str:id>
        pass

    def destroy(self, request, pk=None):  # /api/posts/<str:id>
        pass
