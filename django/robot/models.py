from django.db import models
from smart_selects.db_fields import ChainedForeignKey

LIBRARIES = [("RoboSAPiens.DE", "RoboSAPiens.DE"), ("Browser", "Browser")]

class Library(models.Model):
    name = models.CharField(max_length=255)
    doc = models.TextField()

    def __str__(self) -> str:
        return self.name

class LibraryOptionalArgument(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

class Keyword(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    doc = models.TextField()

    def __str__(self) -> str:
        return f"{self.library.name}.{self.name}"

class KeywordPositionalArgument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)

class KeywordOptionalArgument(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

class TestSuite(models.Model):
    name = models.CharField(max_length=255)
    doc = models.TextField()

    def __str__(self) -> str:
        return self.name

class SettingType(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self) -> str:
        return self.name

class SettingArgument(models.Model):
    setting_type = models.ForeignKey(SettingType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value

class SettingOptionalArgument(models.Model):
    test_suite_setting = models.ForeignKey(SettingArgument, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.value

class Setting(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    setting_type = models.ForeignKey(SettingType, on_delete=models.CASCADE)
    argument = ChainedForeignKey(
        SettingArgument, 
        chained_field='setting_type', 
        chained_model_field='setting_type'
    )
    optional_argument = ChainedForeignKey(
        SettingOptionalArgument, 
        chained_field='argument', 
        chained_model_field='test_suite_setting'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_suite', 'setting_type', 'argument'], name='setting_primary_key'
            )
        ]

    def __str__(self) -> str:
        return f"{self.test_suite.name} | {self.setting_type.name}    {self.argument}"

class TestCase(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0, db_index=True)
    name = models.CharField(max_length=255)
    doc = models.TextField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_suite', 'name'], name='testcase_primary_key'
            )
        ]
        ordering = ['index']

    def __str__(self) -> str:
        return f"{self.test_suite.name}.{self.name}"

class KeywordCall(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0, db_index=True)
    return_value = models.CharField(max_length=255, blank=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_case', 'index'], name='keyword_call_primary_key'
            )
        ]
        ordering = ['index']

    def __str__(self) -> str:
        return f"{self.test_case.name}.{self.index}.{self.keyword}"

class KeywordCallPositionalArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    value = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['keyword_call', 'index'], name='keyword_call_positional_argument_primary_key'
            )
        ]
        ordering = ['index']

class KeywordCallOptionalArgument(models.Model):
    keyword_call = models.ForeignKey(KeywordCall, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['keyword_call', 'name'], name='keyword_call_optional_argument_primary_key'
            )
        ]

class RobotExec(models.Model):
    EXEC_STATUS = [
        ("Planned", "Planned"),
        ("Running", "Running"),
        ("Done", "Done")
    ]

    SERVER = [
        ("localhost", "localhost")
    ]

    testsuite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    server = models.CharField(max_length=255, choices=SERVER, default="localhost")
    status = models.CharField(max_length=255, choices=EXEC_STATUS, default="Planned")

    def __str__(self) -> str:
        return f"{self.testsuite.name} @ {self.datetime.strftime('%d.%m.%y %H:%M:%S')}"

class RobotArgument(models.Model):
    name = models.CharField(max_length=255)
    doc = models.TextField()

    def __str__(self) -> str:
        return self.name

class RobotExecOptionalArgument(models.Model):
    robot_exec = models.ForeignKey(RobotExec, on_delete=models.CASCADE)
    argument = models.ForeignKey(RobotArgument, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

class RobotResult(models.Model):
    RESULT = [
        ("PASS", "PASS"),
        ("FAIL", "FAIL"),
        ("SKIP", "SKIP"),
    ]

    robot_exec = models.ForeignKey(RobotExec, on_delete=models.CASCADE)
    result = models.CharField(max_length=255, choices=RESULT)
    output_xml = models.BinaryField()
    log_html = models.BinaryField()
