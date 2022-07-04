from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student


def my_view(request):
    if request.method == 'get':
        return HttpResponse('result')


class MyView(View):
    def get(self, request):

        name = request.GET.get('name', False)
        # print(id)
        students = Student.objects.all()
        if name:
            students = students.filter(name=name)

        students_data = []
        for student in students:
            students_data.append({
                "name":student.name
            })

        # return redirect('https://google.com')

        return render(request, 'students/students.html', {"students":students_data, "show":False })
        # return JsonResponse({"data":students_data})

    def post(self, request):
        name = request.POST.get('name', '')

        print(name)
        print(request.__dict__)
        return HttpResponse(name)




# class MyView(View):
#     def get(self, request, pk):

#         try:
#             student = Student.objects.get(pk=pk)
#             students_data = {
#                 "name":student.name
#             }
#         except Student.DoesNotExist:
#             students_data = {}
        
#         return JsonResponse({"data":students_data})
