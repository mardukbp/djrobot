from django.db import models
from testplan.models import TestPlan

class TestExecution(models.Model):
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE, related_name='test_executions')
    datetime = models.DateTimeField()
    result = models.CharField(max_length=255, default="Not executed")
    log = models.CharField(max_length=255, default="Not executed")
