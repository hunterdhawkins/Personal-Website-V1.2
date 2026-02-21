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
    resume = models.Documentation.objects.get(document_name="Hunter_Hawkins_Resume_Website")
    print(resume)
    return render(
        request,
        "home/resume.html",
        {
            "resume": resume,
        },
    )


def projects(request):
    # Prefetch the keywords for the project. Reverse foreign key lookup
    # https://medium.com/@soverignchriss/understanding-select-related-and-prefetch-related-methods-in-django-orm-db36003d5fbf
    projects = models.Project.objects.prefetch_related("keywords").order_by('project_name')

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
