from myapp.models import Post,User
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import PostSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from myapp import serializers
from django.core.mail import send_mail
from django.conf import settings

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        serializer.save(author=self.request.user)
        user = User.objects.get(id=self.request.user.id)
        user_email=user.email
        from_email = settings.EMAIL_HOST_USER
        send_mail('Subject aapke hissab de skte ho..... !',
                  '********......Apki Post Upload Ho Chuki Hai.....*********',
                   from_email, 
                  [user_email],
                  fail_silently=False)

    

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


















# class PostListAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


