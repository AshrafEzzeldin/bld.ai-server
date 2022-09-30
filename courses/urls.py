from django.urls import path
from courses.views import Course
from courses.views import OneCourse

urlpatterns = [

    path('', Course.as_view()),
    path('<int:id>', OneCourse.as_view()),
]
