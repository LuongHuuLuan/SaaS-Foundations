

import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    return about_page_view(request, )

def about_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Home page"
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": percent
    }
    PageVisit.objects.create(path=request.path)
    html_template = "home.html"
    return render(request, html_template, my_context)
