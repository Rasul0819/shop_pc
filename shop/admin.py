from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Category)
admin.site.register(models.Product)
