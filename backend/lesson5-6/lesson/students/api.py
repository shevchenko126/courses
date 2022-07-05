from re import L
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from students.models import Student
from rest_framework.authtoken.models import Token
from students.serializers import StudentSerializer, FullStudentSerializer


class GetStudents(viewsets.ModelViewSet):

    # serializer_class = FullStudentSerializer
    queryset = Student.objects.all()
    permissions = (permissions.IsAuthenticatedOrReadOnly(), )

    def get_serializer_class(self, *args, **kwargs):
        token = self.request.headers.get('token', 'u')
        print(token)
        try:
            user = Token.objects.get(key=token).user
            print(user)
            return FullStudentSerializer(*args, **kwargs)
        except Token.DoesNotExist:
            return StudentSerializer(*args, **kwargs)

    def list(self, request):

        students = Student.objects.all()
        students_serialized = self.get_serializer_class(students, many=True).data

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


    def create(self, request):

        name = request.data.get('name', 'u')
        print(name)
        student = Student(
            name=name
        )
        student.save()

        return Response({
            "success":1
        })


    def patch(self, request):

        name = request.data.get('name', 'u')
        token = request.headers.get('token', 'u')
        print(token)

        user = Token.objects.get(key=token).user




        student = Student(
            name=name
        )
        student.save()

        return Response({
            "success":1
        })
