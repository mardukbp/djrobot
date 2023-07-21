# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Library, LibraryOptionalArgument, Keyword, KeywordPositionalArgument, KeywordOptionalArgument, TestSuite, SettingType, SettingArgument, SettingOptionalArgument, Setting, TestCase, KeywordCall, KeywordCallPositionalArgument, KeywordCallOptionalArgument, RobotExec, RobotArgument, RobotExecOptionalArgument, RobotResult


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


@admin.register(SettingType)
class SettingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(SettingArgument)
class SettingArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'setting_type', 'value')
    list_filter = ('setting_type',)


@admin.register(SettingOptionalArgument)
class SettingOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_suite_setting', 'value')
    list_filter = ('test_suite_setting',)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'test_suite',
        'setting_type',
        'argument',
        'optional_argument',
    )
    list_filter = (
        'test_suite',
        'setting_type',
        'argument',
        'optional_argument',
    )


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


@admin.register(RobotExec)
class RobotExecAdmin(admin.ModelAdmin):
    list_display = ('id', 'testsuite', 'datetime', 'server', 'status')
    list_filter = ('testsuite', 'datetime')


@admin.register(RobotArgument)
class RobotArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc')
    search_fields = ('name',)


@admin.register(RobotExecOptionalArgument)
class RobotExecOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'robot_exec', 'argument', 'value')
    list_filter = ('robot_exec', 'argument')


@admin.register(RobotResult)
class RobotResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'robot_exec', 'result', 'output_xml', 'log_html')
    list_filter = ('robot_exec',)
