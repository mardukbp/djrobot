from django.db import models
from robotkw.models import Keyword
from taggit_selectize.managers import TaggableManager
  

def next_keywordcall_index():
    last_entry = KeywordCall.objects.all().order_by('index').last()

    if not last_entry:
        return 0
    
    return last_entry.index + 1


class TestCase(models.Model):
    name = models.CharField(max_length=255)
    tags = TaggableManager()
    documentation = models.TextField()

    def __str__(self) -> str:
        return self.name

class KeywordCall(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=next_keywordcall_index, db_index=True)
    return_value = models.CharField(max_length=255, blank=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.test_case.name} | Keyword Call {self.index}"

class KeywordCallArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class KeywordCallOptionalArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
