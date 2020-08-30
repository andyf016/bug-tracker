from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myuser.models import CustomUser

UserAdmin.fieldsets += ('Custom fields set', {'fields': ['bio']}),
admin.site.register(CustomUser, UserAdmin)
