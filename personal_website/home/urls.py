from django.urls import path
from home import views


urlpatterns = [
    path("", views.home, name='home-home'),
    path("resume/", views.resume, name='home-resume'),
    path("projects/", views.projects, name='home-projects'),
    path("sources/", views.sources, name='home-sources'),

    path("documentation/<str:filename>/", views.pdf_view, name="home-view-pdf"),
]
