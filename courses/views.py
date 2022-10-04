from rest_framework import status
from courses.models import Course as CourseModel
from courses.models import User as UserModel

from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response


class User(APIView):

    def get(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Course(APIView):

    def get(self, request):
        queryset = CourseModel.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class OneCourse(APIView):

    def get(self, request, id):
        try:
            serializer = CourseSerializer(
                CourseModel.objects.filter(id=id)[0])
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def delete(self, request, id):
        try:
            serializer = CourseSerializer(
                CourseModel.objects.get(pk=id).delete())
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'deleted'})

    def put(self, request, id):
        serializer = CourseSerializer(data=request.data, instance=CourseModel.objects.get(pk=id), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DurationCourse(APIView):
    def get(self, request, duration):
        try:
            serializer = CourseSerializer(
                CourseModel.objects.filter(duration=duration), many=True)
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
