from rest_framework import serializers
from blog.models import Article, Comment, Vote


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

