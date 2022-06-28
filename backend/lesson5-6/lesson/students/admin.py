from django.contrib import admin
from students.models import Student, StudentGroup


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group', 'students_number_in_group')
    search_fields = ('name', 'surname', 'group__students_number')
    # ordering = ('name', 'students_number_in_group')

    def students_number_in_group(self, obj):
        if obj.group:
            return obj.group.students_number
        else:
            return ''
    students_number_in_group.short_description = 'Students number in group'
    students_number_in_group.admin_order_field = 'group__students_number'


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup)