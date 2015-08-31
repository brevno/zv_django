from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Student: ' + self.name

    def average_rate(self):
        return Rating.average_rate(student=self)


class Course(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Course: ' + self.name

    def average_rate(self):
        return Rating.average_rate(course=self)


class Rating(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    rate = models.IntegerField(default=0)

    @staticmethod
    def average_rate(student=None, course=None):
        filter = {k: v for k, v in locals().items() if v}
        return Rating.objects.filter(**filter).aggregate(avg_rate=models.Avg('rate'))['avg_rate']
