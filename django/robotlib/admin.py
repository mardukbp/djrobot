# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Library, OptionalArgument


class OptionalArgumentInline(admin.TabularInline):
    model = OptionalArgument
    extra = 0


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'documentation')
    inlines = [OptionalArgumentInline]

@admin.register(OptionalArgument)
class OptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'library', 'name', 'default_value')
    list_filter = ('library',)
    search_fields = ('name',)
