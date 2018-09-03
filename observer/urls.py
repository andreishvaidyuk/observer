from django.urls import path
from observer import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('students/', views.student_list, name="students_list"),
    path('student/(?P<pk>\d+)/', views.student_detail, name="student_detail"),
    path('student/new/', views.add_student, name="add_student"),
    path('^student/(?P<pk>\d+)/edit/$', views.edit_student, name="edit_student"),
    # path('^student/(?P<pk>\d+)/delete/$', views.delete_student, name="delete_student"),
]