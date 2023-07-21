from django.db import models
from robotlib.models import Library

class Keyword(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    documentation = models.TextField()

    def __str__(self) -> str:
        return f"{self.library.name}.{self.name}"

class Argument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)

class OptionalArgument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)
