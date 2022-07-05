from rest_framework import serializers
from students.models import Student, StudentGroup

class GroupSerializer(serializers.ModelSerializer):

    is_full = serializers.SerializerMethodField()

    class Meta:
        model = StudentGroup
        fields = ['name', 'is_full']

    def get_is_full(self, obj):
        if obj.students_number > 30:
            return True
        return False


class StudentSerializer(serializers.ModelSerializer):

    birthday_dots = serializers.SerializerMethodField()
    group_name = GroupSerializer(source='group')

    class Meta:
        model = Student
        fields = ['name', 'birthday_dots', 'group_name']
        


    def get_birthday_dots(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d.%m.%Y")
        else:
            return ''



class FullStudentSerializer(StudentSerializer):

    class Meta:
        model = Student
        fields = StudentSerializer.Meta.fields + ['group']
        depth = 1
