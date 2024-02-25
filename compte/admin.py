from django.contrib import admin
from django.contrib.auth.admin import Group

# Register your models here.

admin.site.unregister(Group)
