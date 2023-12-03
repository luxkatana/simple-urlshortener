from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from . import models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "mainapp/index.html")


def create_link(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        formdata = request.POST
        redirect_url = formdata.get("redirect_url", None)
        if redirect_url:
            new_url = models.Url(link=redirect_url)
            print(new_url)
            new_url.save()
            return render(request, "mainapp/success.html", {"url": redirect_url})
    return redirect("/index")


def redirect_to_matching(request: HttpRequest, targetid: int) -> HttpResponse:
    try:
        matching = models.Url.objects.get(id=targetid)
        matching.visits +=1
        matching.save()
        return redirect(matching.link)
    except: # noqa
        response = render(request, "mainapp/invalidid.html")
        response.status_code = 404
        return response


def overview_of_shortener(request: HttpRequest, targetid: int) -> HttpResponse:
    try:
        matching = models.Url.objects.get(id=targetid)
        return render(request, "mainapp/overview.html", context={'matching': matching})
    except Exception: # noqa
        response = render(request, "mainapp/invalidid.html")
        response.status_code = 404
        return response


