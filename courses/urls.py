from django.urls import path
from courses.views import Course

urlpatterns = [

    path('',Course.as_view()),
    path('<int:id>', Course.as_view()),
]