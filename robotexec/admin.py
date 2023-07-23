# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TestExecution


@admin.register(TestExecution)
class TestExecutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_plan', 'datetime', 'result', 'log')
    list_filter = ('test_plan', 'datetime')
