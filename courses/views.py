from django.http import HttpResponse
from django.utils.timezone import activate
from rest_framework import viewsets, generics, permissions
from courses.models import Category, Course
from courses import serializers

def index(request):
    return HttpResponse('Hello, World!')

class CategoryView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active = True)
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
