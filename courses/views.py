from django.views import View
import json
from django.http import JsonResponse
from courses.models import Course as CourseModel
from django.forms.models import model_to_dict


class Course(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(list(CourseModel.objects.values().order_by("name")), safe=False)



    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        c = CourseModel(name=body["name"], description=body["description"])
        c.save()
        return JsonResponse(model_to_dict(c))

    def put(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        c = CourseModel.objects.filter(pk=body['id'])
        if len(c) == 0:
            return JsonResponse("NO OBJECT", safe=False)
        c = c[0]
        if body['name']:
            c.name = body['name']
        if body['description']:
            c.description = body['description']
        c.save()
        return JsonResponse("done", safe=False)


class OneCourse(View):

    def get(self, request, *args, **kwargs):
        c = CourseModel.objects.filter(pk=kwargs['id'])
        if len(c) == 0:
            return JsonResponse("NO OBJECT", safe=False)
        return JsonResponse(model_to_dict(c[0]))

    def delete(self, request, *args, **kwargs):
        item = CourseModel.objects.filter(id=kwargs['id']).delete()
        return JsonResponse("deleted", safe=False) if item[0] != 0 else JsonResponse("no record found", safe=False)


class DurationCourse(View):
    def get(self, request, *args, **kwargs):
        c = list(CourseModel.objects.filter(duration__gt=kwargs['duration']).values())
        return JsonResponse(c, safe=False)
