from myapp.models import Post
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import PostSerializer
from rest_framework import generics
from rest_framework import mixins


# class PostListAPIView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


class PostAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer