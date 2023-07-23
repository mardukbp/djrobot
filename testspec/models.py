from django.db import models
import robotkw.models
from testplan.models import TestPlan
from taggit_selectize.managers import TaggableManager


class TestCase(models.Model):
    name = models.CharField(max_length=255)
    tags = TaggableManager()
    test_plans = models.ManyToManyField(TestPlan, related_name='test_cases', blank=True)
    documentation = models.TextField()

    def __str__(self) -> str:
        return self.name

class KeywordCall(robotkw.models.KeywordCall):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name='keyword_calls')

    def __str__(self) -> str:
        return f"{self.test_case.name} | {self.index} {self.keyword_name}"

class KeywordCallArgument(robotkw.models.KeywordCallArgument):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE, related_name='args')

class KeywordCallOptionalArgument(robotkw.models.KeywordCallOptionalArgument):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE, related_name='kwargs')
