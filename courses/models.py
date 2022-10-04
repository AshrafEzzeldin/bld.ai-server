from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    duration = models.IntegerField()
    file = models.FileField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.first_name
