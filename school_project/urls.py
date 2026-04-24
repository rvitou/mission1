from django.contrib import admin
from django.urls import path
from school_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-course/', views.register_course, name='register_course'),
    path('add-student/', views.register_student, name='register_student'),
    path('report/', views.report, name='report'),
]
