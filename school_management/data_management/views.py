from rest_framework import viewsets
from .models import Student, Subject, Grade
from .serializers import StudentSerializer, SubjectSerializer, GradeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the School Management System!")