from django.db import models

# Create your models here.
# class School(models.Model):
#     name=models.CharField(max_length=250)
#     def __str__(self):
#         return self.name
#
# class Dept(models.Model):
#     dept_name=models.CharField(max_length=250)
#
#     def __str__(self):
#         return '{}'.format(self.dept_name)
#
# class Course(models.Model):
#     course_name=models.CharField(max_length=250)
#     time_period=models.IntegerField(default=2)
#     department = models.ForeignKey(Dept, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{}'.format(self.course_name)
class Dept(models.Model):
    dept_name=models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.dept_name)

class Course(models.Model):
    course_name=models.CharField(max_length=250)
    time_period=models.IntegerField()
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.course_name)