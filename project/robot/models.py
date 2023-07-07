from django.db import models

class TestSuite(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class TestCase(models.Model):
    name = models.CharField(max_length=255)
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class KeywordCall(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    return_value = models.CharField(max_length=255, blank=True)
    keyword = models.CharField(max_length=255)
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)
    arg3 = models.CharField(max_length=255, blank=True)
    arg4 = models.CharField(max_length=255, blank=True)
    arg5 = models.CharField(max_length=255, blank=True)
 