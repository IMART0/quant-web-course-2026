from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404

def main_page(request):


    html = ''

    for i, j in COURSES.items():
        print(i, j)
        html += \
            f"<li><a href='courses/{i}/'>{i}</a></li>"


    return render(request, './base.html', context={'courses': COURSES.items()})

    return HttpResponse(
        f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Квант</title>
</head>
<body>
    <h1>Добро пожаловать на сайт Кванта</h1>
    <h2>Наши курсы</h2>
    
    <ul>
        {html}
    </ul>
</body>
</html>
    


        """
        )


COURSES = {
    "Олимпиадное_программирование" : "Олимп прога в Кванте",
    "Веб-разработка на Python" : "2",
    "Физмат 7" : "3",
    "Физмат 8" : "4",
    "Физмат 9" : "5",
}

def courses(request, course_name):
    if course_name not in COURSES:
        return HttpResponse(
            f"курса {course_name} нет",
            status=404,
        )

    return HttpResponse(COURSES[course_name])