from django.db import models
import robotkw.models

class ResourceKeyword(robotkw.models.Keyword):
    return_value = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name

class Argument(robotkw.models.Argument):
    keyword = models.ForeignKey(ResourceKeyword, on_delete=models.CASCADE)

    @property
    def rf_name(self):
        return "${" + self.name + "}"

class OptionalArgument(robotkw.models.OptionalArgument):
    keyword = models.ForeignKey(ResourceKeyword, on_delete=models.CASCADE)

    @property
    def rf_name(self):
        return "${" + self.name + "}"

class KeywordCall(robotkw.models.KeywordCall):
    calling_keyword = models.ForeignKey(ResourceKeyword, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.calling_keyword.name} | {self.index} {self.keyword_name}"

class KeywordCallArgument(robotkw.models.KeywordCallArgument):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)

class KeywordCallOptionalArgument(robotkw.models.KeywordCallOptionalArgument):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
