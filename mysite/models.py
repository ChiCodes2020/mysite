from django.db import models

class Teacher(models.Model):
    teacher_id = models.IntegerField(primarykey = True),
    teacher_name = models.CharField(max_length=100)



class Course(models.Model):
    course_id = models.IntegerField(rimarykey = True),
    course_name = models.CharField(max_length=200),
    teacher_id = models.ForeignKey(Teacher)
