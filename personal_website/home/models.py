from django.db import models
from django.utils.text import slugify


# Create your models here.
class Documentation(models.Model):
    document = models.FileField(upload_to="documentation", blank=True, null=True)
    document_name = models.TextField(default="", unique=True)
    published_at = models.DateTimeField()


class Project(models.Model):
    project_name = models.CharField(default="", max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    project_location = models.TextField(default="")
    project_short_description = models.TextField(default="")
    project_description = models.TextField(default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)


class TechnologyUsed(models.Model):
    name = models.CharField(default="", max_length=64)
    project = models.ForeignKey(Project, related_name="keywords", on_delete=models.CASCADE)


class ProjectPhotos(models.Model):
    image = models.ImageField(upload_to="images/")
    image_description = models.TextField(default="", blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PersonalPhotos(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.TextField(default="", unique=True)
