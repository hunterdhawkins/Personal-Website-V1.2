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
    projects = models.Project.objects.all()

    return render(
        request,
        "home/projects.html",
        {
            "projects": projects,
        },
    )


def individual_project(request, slug):
    project = models.Project.objects.get(slug=slug)
    photos = models.ProjectPhotos.objects.filter(project=project)

    return render(
        request,
        "home/individual_project.html",
        {
            "project": project,
            "photos": photos,
        },
    )


def sources(request):

    return render(
        request,
        "home/sources.html",
        {
        },
    )


# https://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view
def pdf_view(request, filename):
    # There is probably a better way to query that just returns the single object
    document = models.Documentation.objects.get(document_name=filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'documentation', document.document_name)

    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
