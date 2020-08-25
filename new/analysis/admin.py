from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import All


@admin.register(All)
class AllAdmin(ImportExportModelAdmin):
	pass


