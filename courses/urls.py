from django.urls import path

from courses.views import *

urlpatterns = [

    path('users', User.as_view()),
    path('', Course.as_view()),
    path('<int:id>', OneCourse.as_view()),
    path('Duration/<int:duration>', DurationCourse.as_view()),

]
