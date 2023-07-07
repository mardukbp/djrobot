from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=255)
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)
    arg3 = models.CharField(max_length=255, blank=True)
    arg4 = models.CharField(max_length=255, blank=True)
    arg5 = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name


class TestSuite(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

SETTINGS = [
    ("Library", "Library")
]


class Settings(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, choices=SETTINGS, default="Library")
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)
    arg3 = models.CharField(max_length=255, blank=True)
    arg4 = models.CharField(max_length=255, blank=True)
    arg5 = models.CharField(max_length=255, blank=True)


class TestCase(models.Model):
    name = models.CharField(max_length=255)
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Keyword(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    method_name = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)
    arg3 = models.CharField(max_length=255, blank=True)
    arg4 = models.CharField(max_length=255, blank=True)
    arg5 = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.library.name}.{self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['library', 'name'], name='unique_keyword_name_per_library'
            )
        ]


class KeywordCall(models.Model):
    index = models.PositiveSmallIntegerField(default=1)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    return_value = models.CharField(max_length=255, blank=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)
    arg3 = models.CharField(max_length=255, blank=True)
    arg4 = models.CharField(max_length=255, blank=True)
    arg5 = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_case', 'index'], name='unique_keyword_call_per_test_case'
            )
        ]
