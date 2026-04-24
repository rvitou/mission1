from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    # Remove 'on_python_objects=True' -> This was causing the error
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
