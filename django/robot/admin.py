# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Library, TestSuite, Settings, TestCase, Keyword, KeywordCall


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'arg1', 'arg2', 'arg3', 'arg4', 'arg5')
    search_fields = ('name',)


@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'test_suite',
        'name',
        'arg1',
        'arg2',
        'arg3',
        'arg4',
        'arg5',
    )
    list_filter = ('test_suite',)
    search_fields = ('name',)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'test_suite')
    list_filter = ('test_suite',)
    search_fields = ('name',)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'library',
        'method_name',
        'name',
        'arg1',
        'arg2',
        'arg3',
        'arg4',
        'arg5',
    )
    list_filter = ('library',)
    search_fields = ('name',)


@admin.register(KeywordCall)
class KeywordCallAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'index',
        'test_case',
        'return_value',
        'keyword',
        'arg1',
        'arg2',
        'arg3',
        'arg4',
        'arg5',
    )
    list_filter = ('test_case', 'keyword')
