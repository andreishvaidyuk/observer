from django.urls import path
from observer import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('students/', views.student_list, name="students_list"),
    path('student/new/', views.add_student, name="add_student"),
    path('student/(?P<pk>\d+)/', views.student_detail, name="student_detail"),
    path('^student/(?P<pk>\d+)/edit/$', views.edit_student, name="edit_student"),
    path('sections/', views.section_list, name="sections_list"),
    path('section/new/', views.add_section, name="add_section"),
    path('section/(?P<pk>\d+)/', views.section_detail, name="section_detail"),
    path('^section/(?P<pk>\d+)/edit/$', views.edit_section, name="edit_section"),
    path('ajax/load_sections/', views.load_section, name="ajax_load_sections"),
    path('group/', views.group_list, name="group_list"),
    path('group/new/', views.add_group, name="add_group"),
    path('group/(?P<pk>\d+)/', views.group_detail, name="group_detail"),
    path('^group/(?P<pk>\d+)/edit/$', views.edit_group, name="edit_group"),
    path('ajax/load_groups/', views.load_group, name="ajax_load_groups"),
    path('filial/', views.filial_list, name="filial_list"),
    path('filial/new/', views.add_filial, name="add_filial"),
    path('filial/(?P<pk>\d+)/', views.filial_detail, name="filial_detail"),
    path('^filial/(?P<pk>\d+)/edit/$', views.edit_filial, name="edit_filial"),
    # path('^student/(?P<pk>\d+)/delete/$', views.delete_student, name="delete_student"),
]