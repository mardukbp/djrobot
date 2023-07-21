# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Keyword, Argument, OptionalArgument

class ArgumentInline(admin.TabularInline):
    model = Argument
    extra = 0

class OptionalArgumentInline(admin.TabularInline):
    model = OptionalArgument
    extra = 0

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'library', 'name', 'documentation')
    list_filter = ('library',)
    search_fields = ('name',)
    inlines = [ArgumentInline, OptionalArgumentInline]

@admin.register(Argument)
class ArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'position', 'name')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(OptionalArgument)
class OptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'name', 'default_value')
    list_filter = ('keyword',)
    search_fields = ('name',)
