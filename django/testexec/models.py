from django.db import models
from robotlib.models import Library

class TestSuite(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class LibraryImport(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.test_suite.name} | {self.library.name}"

class LibraryImportArgument(models.Model):
    import_library = models.ForeignKey(LibraryImport, on_delete=models.CASCADE)
    argument = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
