from django.shortcuts import render
from django.http import HttpResponse

dict = {
    "cpp": "si plus plus",
    "python": "pyton"
}

def main_page(request):
    html = ""

    for name, desc in dict.items():
        html += f'<li><a href="courses/{name}/">{name}</a></li>'

    return render(request, 'templates/base.html', context={"courses": list(dict.items())})

def course_choice(request):
    return HttpResponse("""
<h1>Выбор курса</h1>
<ul>
    <li><a href="courses/cpp">сипп</a></li>
    <li><a href="courses/python">pyton</a></li>
</ul>
""")

def course_page(request, course_name):
    if course_name not in dict:
        return HttpResponse(f"нету {course_name}", status=200)
    return HttpResponse(dict[course_name])