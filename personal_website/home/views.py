# Python imports
import os
# Django Imports
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
# App Imports
from home import utils, models


def home(request):

    return render(
        request,
        "home/home.html",
        {
        },
    )


def resume(request):

    return render(
        request,
        "home/resume.html",
        {
        },
    )


def projects(request):

    return render(
        request,
        "home/projects.html",
        {
        },
    )


# https://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view
def pdf_view(request, filename):
    print(filename)
    document = models.Documentation.objects.filter(document_name=filename)
    print(document)
    try:
        document = document[0]
    except IndexError:
        raise Http404()
    print(document.document_name)
    file_path = os.path.join(settings.MEDIA_ROOT, 'documentation', document.document_name)

    # print(file_path)
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
