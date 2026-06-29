from django.urls import path

from main import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('courses/<str:course_name>/',
         views.course_description, name='description')
]