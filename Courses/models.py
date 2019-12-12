from django.db import models

class Courses(models.Model):

    course_code=models.CharField(max_length=10, null=True, blank=True)

    course_title=models.CharField(max_length=200, null=True, blank=True)

    course_credit=models.IntegerField(default=0)

    elective=models.BooleanField(default=False)

 

    def __str__(self):

         return self.course_title