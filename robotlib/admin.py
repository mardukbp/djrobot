# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Library, InitArgument, LibraryKeyword, KeywordArgument, KeywordOptionalArgument


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version')
    search_fields = ('name',)


@admin.register(InitArgument)
class InitArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'library', 'name', 'default_value')
    list_filter = ('library',)
    search_fields = ('name',)


@admin.register(LibraryKeyword)
class LibraryKeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'library', 'tag')
    list_filter = ('library',)
    search_fields = ('name',)


@admin.register(KeywordArgument)
class KeywordArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name', 'keyword')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(KeywordOptionalArgument)
class KeywordOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'default_value', 'keyword')
    list_filter = ('keyword',)
    search_fields = ('name',)
