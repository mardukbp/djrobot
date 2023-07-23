# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ResourceKeyword, Argument, OptionalArgument, KeywordCall, KeywordCallArgument, KeywordCallOptionalArgument


@admin.register(ResourceKeyword)
class ResourceKeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'documentation', 'return_value')
    search_fields = ('name',)


@admin.register(Argument)
class ArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name', 'keyword')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(OptionalArgument)
class OptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'default_value', 'keyword')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(KeywordCall)
class KeywordCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'return_value', 'keyword_name', 'calling_keyword')
    list_filter = ('calling_keyword',)


@admin.register(KeywordCallArgument)
class KeywordCallArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'value', 'keyword_call')
    list_filter = ('keyword_call',)


@admin.register(KeywordCallOptionalArgument)
class KeywordCallOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'keyword_call')
    list_filter = ('keyword_call',)
    search_fields = ('name',)
