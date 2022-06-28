from django.contrib import admin
from django.urls import path, include
from students.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', my_view),
    path('students/', include('students.urls')),
    path('', my_view),
]
