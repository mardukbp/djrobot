from django.db import models
from robotlib.models import Library


class TestPlan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class LibraryImport(models.Model):
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE, related_name='library_imports')
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["test_plan", "library"],
                name="unique_library_import"
            )
        ]

    def __str__(self) -> str:
        return f"{self.test_plan.name} | {self.library.name}"

class LibraryImportArgument(models.Model):
    library_import = models.ForeignKey(LibraryImport, on_delete=models.CASCADE, related_name='arguments')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
