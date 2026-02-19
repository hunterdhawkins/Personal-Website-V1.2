from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home-home'),
    path("resume/", views.resume, name='home-resume'),
    path("projects/", views.projects, name='home-projects'),
    path("sources/", views.sources, name='home-sources'),
    path("project/<str:slug>/", views.individual_project, name="home-individual-project"),

    path("documentation/<str:filename>/", views.pdf_view, name="home-view-pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
