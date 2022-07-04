from re import L
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from students.models import Student
from students.serializers import StudentSerializer


class GetStudents(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request):

        students = Student.objects.all()
        students_serialized = self.serializer_class(students, many=True).data

        return Response({
            "success":1,
            "students":students_serialized
        })

    def get_object(self):
        slug = int(self.kwargs['pk'])
        print(slug)
        student = Student.objects.filter(id=slug)
        obj = get_object_or_404(student)
        return obj