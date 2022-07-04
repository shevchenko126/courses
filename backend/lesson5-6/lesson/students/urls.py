from rest_framework import routers
from django.contrib import admin
from django.urls import path
from students.views import MyView
from students.api import GetStudents


router = routers.DefaultRouter()
router.register('api', GetStudents, 'api')


urlpatterns = router.urls + [
    path('view1/', MyView.as_view()),
    path('view2/<pk>/', MyView.as_view()),
    path('view3/', MyView.as_view(), 'view3'),
]
