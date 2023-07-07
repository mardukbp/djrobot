# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TestSuite, TestCase, KeywordCall


@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'test_suite')
    list_filter = ('test_suite',)
    search_fields = ('name',)


@admin.register(KeywordCall)
class KeywordCallAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'return_value',
        'keyword',
        'arg1',
        'arg2',
        'arg3',
        'arg4',
        'arg5',
        'test_case',
    )
    list_filter = ('test_case',)
