from rest_framework import serializers
from .models import *

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ['id', 'username', 'is_staff']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['comment_on_course'] = CourseSerializer(read_only=True)
        self.fields['comment_user'] = SimpleUserSerializer(read_only=True)
        return super(CommentSerializer, self).to_representation(instance)
