from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm
from .models import Student, Course

# Form 1: Student Register
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

# Form 2: Course Register
def register_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_student')
    else:
        form = CourseForm()
    return render(request, 'register_course.html', {'form': form})

# Report: List students per course
def report(request):
    courses = Course.objects.all()
    # We pass courses to the template so we can list students under them
    return render(request, 'report.html', {'courses': courses})
