from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=255)
    documentation = models.TextField()

    class Meta:
        abstract = True


class Argument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class OptionalArgument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

    class Meta:
        abstract = True


class KeywordCall(models.Model):
    index = models.PositiveSmallIntegerField(default=0, db_index=True)
    return_value = models.CharField(max_length=255, blank=True)
    keyword_name =  models.CharField(max_length=255)

    class Meta:
        abstract = True


class KeywordCallArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0)
    value = models.CharField(max_length=255)

    class Meta:
        abstract = True


class KeywordCallOptionalArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        abstract = True
