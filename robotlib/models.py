from django.db import models
import robotkw.models


class Library(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    documentation = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Libraries"

        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_library"
            )
        ]


class InitArgument(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='arguments')
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)


class LibraryKeyword(robotkw.models.Keyword):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='keywords')
    tag = models.CharField(max_length=255, blank=True)

    @property
    def full_name(self):
        return f"{self.library.name}.{self.name}"

    def __str__(self) -> str:
        return self.full_name


class KeywordArgument(robotkw.models.Argument):
    keyword = models.ForeignKey(LibraryKeyword, on_delete=models.CASCADE, related_name='args')


class KeywordOptionalArgument(robotkw.models.OptionalArgument):
    keyword = models.ForeignKey(LibraryKeyword, on_delete=models.CASCADE, related_name='kwargs')
