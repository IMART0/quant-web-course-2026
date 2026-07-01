from main import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('teachers/<str:teacher_link>', views.teacher_page, name='teacher_page'),
    path('courses/<str:course_name>', views.course_page, name='course_page')
]