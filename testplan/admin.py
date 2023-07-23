# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import TestPlan, LibraryImport, LibraryImportArgument


@admin.register(TestPlan)
class TestPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(LibraryImport)
class LibraryImportAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_plan', 'library')
    list_filter = ('test_plan', 'library')


@admin.register(LibraryImportArgument)
class LibraryImportArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'library_import', 'name', 'value')
    list_filter = ('library_import',)
