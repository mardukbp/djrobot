from django.contrib import admin
from .models import LibraryImport, TestSuite, LibraryImportArgument


class LibraryImportInline(admin.StackedInline):
    model = LibraryImport
    extra = 1


@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [LibraryImportInline]


@admin.register(LibraryImport)
class LibraryImportAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_suite', 'library')
    list_filter = ('test_suite', 'library')


@admin.register(LibraryImportArgument)
class LibraryImportArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'import_library', 'argument', 'value')
    list_filter = ('import_library',)
