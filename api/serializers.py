from api.models import Posts,Comments
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self, validated_data):                                                                          #overided because to hash/secure password , by default the orm query is objects.create
        return User.objects.create_user(**validated_data)

class PostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    liked_by=UserSerializer(many=True,read_only=True)
    like_count=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        exclude=('date',)

    def create(self, validated_data):
        user=self.context.get("usr")
        return Posts.objects.create(**validated_data,user=user)

class CommentSerializer(serializers.ModelSerializer):
    post=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        fields=["post","comment","user"]
    def create(self, validated_data):
        user=self.context.get("user")
        post=self.context.get("post")
        return Comments.objects.create(**validated_data,user=user,post=post)







