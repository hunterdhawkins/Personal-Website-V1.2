from django.contrib import admin
from home import models

# Register your models here.
admin.site.register(models.Documentation)
admin.site.register(models.Project)
admin.site.register(models.TechnologyUsed)
admin.site.register(models.ProjectPhotos)
