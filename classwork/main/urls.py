from main import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('courses/<str:course_name>', views.course_page, name='course_page'),
    path('courses', views.course_choice, name='course_choice')
]