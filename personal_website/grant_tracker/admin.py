from django.contrib import admin
from grant_tracker import models

# Register your models here.
admin.site.register(models.Grant)
admin.site.register(models.GrantActivityLog)
admin.site.register(models.GrantDocuments)
