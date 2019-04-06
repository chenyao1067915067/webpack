from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title','author','content','created','category','tags')