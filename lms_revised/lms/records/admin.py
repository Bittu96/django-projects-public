from django.contrib import admin

from . import models


admin.site.register(models.Thing)
admin.site.register(models.Item)

