from rest_framework import serializers
from posts.models import Comment, Group, Post, User
import re


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post',)


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        ref_name = 'ReadOnlyUsers'

    def validate_email(self, value):
        if not re.match(
            r'^[\w.\-]{1,25}@[\w]{1,10}\.(by|ru|ua|com)$',
            value
        ):
            raise serializers.ValidationError('wrong email')
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user exists')
        return value

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        if not any([first_name, last_name]):
            raise serializers.ValidationError(
                'first_name or last_name required')
        return attrs


class PostSerializer(serializers.ModelSerializer):

    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)
