# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TestCase, KeywordCall, KeywordCallArgument, KeywordCallOptionalArgument


class KeywordCallInline(admin.StackedInline):
    model = KeywordCall
    extra = 0
    fields = ('return_value', 'keyword')


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_list', 'documentation')
    search_fields = ('name',)
    inlines = [KeywordCallInline]

    #using prefetch_related() to minimize queries as recommed in official docs
    #https://django-taggit.readthedocs.io/en/latest/admin.html#including-tags-in-modeladmin-list-display
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(KeywordCall)
class KeywordCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_case', 'index', 'keyword', 'return_value')
    list_filter = ('test_case', 'keyword')


@admin.register(KeywordCallArgument)
class KeywordCallArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword_call', 'position', 'name', 'value')
    list_filter = ('keyword_call',)
    search_fields = ('name',)


@admin.register(KeywordCallOptionalArgument)
class KeywordCallOptionalArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword_call', 'name', 'value')
    list_filter = ('keyword_call',)
    search_fields = ('name',)
