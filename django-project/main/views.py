from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse

COURSES = {
    # "Python": "Здесь изучаем питон",
    # "plusy": "Здесь изучаем плюсы",
    # "Super_course": "Здесь изучаем что такое супер",
    # "Tatar_language": "учим татарский"
}

TEACHER = {
    'name': 'raushan'
}

def main_page(request):

    return render(request, './base.html', context={
        'courses': list(COURSES.items()),
        'teacher': TEACHER
    })

def course_description(request, course_name):

    if course_name not in COURSES:
        return HttpResponse(
            f"курса {course_name} нет",
            status=404
        )

    return HttpResponse(
        COURSES[course_name]
    )