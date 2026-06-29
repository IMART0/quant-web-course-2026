from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

COURSES = {
    "python": "изучение основ python и фреймворка django ",
    "c++": "для олимпиадного программирования",
    "html/css": "для вёрстки сайтов",
    "Фреймворк django": "Для создания веб-приложений",
}

def main_page(request):
    # return HttpResponse("Добро пожаловать на сайт Кванта")
    html = ""

    for slug, _ in COURSES.items():
        html += \
            f"<li><a href = 'courses/{slug}'>{slug}</a></li>\n"
    return render(request, '/base.html', context=("", COURSES))
        
    return HttpResponse(

    f"""
<!DOCTYPE html
<html>
<head>
    <meta charset="UTF-8">
    <title>Квант</title>
</head>
<body>
    <h1>Добро пожаловать на сайт Квант</h1>
    <h2>Наши курсы</h2>
    
    <ul>
        {html}
    </ul>

</body>
</html>
    """
    )

# def courses(request, course_name):
    # return HttpResponse(COURSES[course_name])

def courses(request, course_name):

    # Желательно использовать raise, а не return
    if course_name not in COURSES:
        raise Http404(f"Курса {course_name} нет")
    
    if course_name not in COURSES:
        return HttpResponse(
            f"курса {course_name} нет",
            status=404
        )
    
    return HttpResponse(
        COURSES[course_name]
    )