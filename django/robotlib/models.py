from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    documentation = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Libraries"

class OptionalArgument(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)
