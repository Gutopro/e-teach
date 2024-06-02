from rest_framework import serializers
from ..models.course_project import CourseProject

class CourseProjectSerializer(serializers.ModelSerializer):
    """Serializer for course_project model"""
    class Meta:
        model = CourseProject
        fields = '__all__'

class CourseProjectUpdateSerializer(CourseProjectSerializer):
    """Serializer for updating existing Course project"""
    class Meta:
        model = CourseProject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseProjectUpdateSerializer, self).__init__(*args, **kwargs)
        # Make field optional when updating
        for field_name, field in self.fields.items():
            field.required = False
