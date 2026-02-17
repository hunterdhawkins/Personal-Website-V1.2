from django.db import models


# Create your models here.
class Documentation(models.Model):
    document = models.FileField(upload_to="documentation", blank=True, null=True)
    document_name = models.TextField(default="")
    published_at = models.DateTimeField()


class Project(models.Model):
    project_name = models.TextField(default="")
    project_location = models.TextField(default="")
    project_description = models.TextField(default="")


class TechnologyUsed(models.Model):
    name = models.CharField(default="", max_length=64)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectPhotos(models.Model):
    image = models.FileField(upload_to="images", blank=True, null=True)
    image_name = models.TextField(default="")
