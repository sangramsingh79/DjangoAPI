from rest_framework import routers, serializers
from .models import Student
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"