from django.views import View
import json
from django.http import JsonResponse

f = open('courses/db.json')
data = json.load(f)


class Course(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data.update(body)
        with open('courses/db.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data.update(body)
        with open('courses/db.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)
        return JsonResponse(data)


class OneCourse(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(data[str(kwargs['id'])] if str(kwargs['id']) in data.keys() else
                            {"error": "error"})

    def delete(self, request, *args, **kwargs):
        data.pop(str(kwargs['id']), None)
        with open('courses/db.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)
        return JsonResponse(data)
