from rest_framework import serializers
from .models import Post,User

class PostSerializer(serializers.ModelSerializer):	
	author = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Post
		fields = ('title', 'description', 'pic', 'author') 


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','password', 'posts']

