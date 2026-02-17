from django.db import models


# Create your models here.
class Documentation(models.Model):
    document = models.FileField(upload_to="documentation", blank=True, null=True)
    document_name = models.TextField(default="")
    published_at = models.DateTimeField()
