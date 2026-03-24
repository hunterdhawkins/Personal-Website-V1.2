from django.db import models
from django.utils.text import slugify


# Create your models here.
class Grant(models.Model):
    GrantType = models.TextChoices("Precision Agriculture", "AI in Manufacturing", "Power", "Robotics")
    type = models.CharField(blank=True, choices=GrantType)
    StatusType = models.TextChoices("Just Found", "Application in Progress", "Accepted", "Rejected")
    status = models.CharField(blank=True, choices=StatusType)
    grant_name = models.TextField()
    grant_url = models.URLField()
    found_date = models.DateTimeField()
    due_date = models.DateTimeField()
    slug = models.SlugField(max_length=128, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)


class GrantActivityLog(models.Model):
    update_text = models.TextField()
    timestamp = models.DateTimeField()
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)


class GrantDocuments(models.Model):
    document = models.FileField(upload_to="documents/")
    document_description = models.TextField(default="", blank=True, null=True)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)