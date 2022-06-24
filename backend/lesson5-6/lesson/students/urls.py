from django.contrib import admin
from django.urls import path
from students.views import MyView

urlpatterns = [
    path('view1/', MyView.as_view()),
    path('view2/<pk>/', MyView.as_view()),
    path('view3/', MyView.as_view()),
]
