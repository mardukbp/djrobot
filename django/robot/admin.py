# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Library, LibraryOptionalArgument, Keyword, KeywordPositionalArgument, KeywordOptionalArgument, TestSuite, Setting, SettingOptionalArgument, TestCase, KeywordCall, KeywordCallPositionalArgument, KeywordCallOptionalArgument


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc')
    search_fields = ('name',)


@admin.register(LibraryOptionalArgument)
class LibraryOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'library', 'name', 'default_value')
    list_filter = ('library',)
    search_fields = ('name',)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'library', 'name', 'doc')
    list_filter = ('library',)
    search_fields = ('name',)


@admin.register(KeywordPositionalArgument)
class KeywordPositionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'index', 'name')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(KeywordOptionalArgument)
class KeywordOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'name', 'default_value')
    list_filter = ('keyword',)
    search_fields = ('name',)


@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc')
    search_fields = ('name',)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_suite', 'index', 'name', 'argument')
    list_filter = ('test_suite',)
    search_fields = ('name',)


@admin.register(SettingOptionalArgument)
class SettingOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'setting', 'name', 'value')
    list_filter = ('setting',)
    search_fields = ('name',)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_suite', 'index', 'name', 'doc')
    list_filter = ('test_suite',)
    search_fields = ('name',)


@admin.register(KeywordCall)
class KeywordCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_case', 'index', 'return_value', 'keyword')
    list_filter = ('test_case', 'keyword')


@admin.register(KeywordCallPositionalArgument)
class KeywordCallPositionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword_call', 'index', 'value')
    list_filter = ('keyword_call',)


@admin.register(KeywordCallOptionalArgument)
class KeywordCallOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword_call', 'name', 'default_value')
    list_filter = ('keyword_call',)
    search_fields = ('name',)
