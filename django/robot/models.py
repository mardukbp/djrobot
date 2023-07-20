from django.db import models

LIBRARIES = [("RoboSAPiens.DE", "RoboSAPiens.DE"), ("Browser", "Browser")]
# RoboSAPiens_ARGS = [("vortragsmodus", "vortragsmodus")]
# Browser_ARGS = [("headless", "headless")]
# LIB_ARGS = [("RoboSAPiens", RoboSAPiens_ARGS), ("Browser", Browser_ARGS)]
# RoboSAPiens = [("RoboSAPiens.DE.Textfeld ausfüllen", "Textfeld ausfüllen")]
# Browser = [("Browser.New Page", "New Page")]
# KEYWORDS = [("RoboSAPiens", RoboSAPiens), ("Browser", Browser)]

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

class Setting(models.Model):
    SETTINGS = [
        ("Library", "Library")
    ]

    ARGUMENTS = [
        ("Library", LIBRARIES)
    ]

    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255, choices=SETTINGS, default="Library")
    argument = models.CharField(max_length=255, choices=ARGUMENTS, default="Library")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_suite', 'name', 'argument'], name='setting_primary_key'
            )
        ]
        ordering = ['index']

    def __str__(self) -> str:
        return f"{self.test_suite.name}.{self.name}.{self.argument}"

class SettingOptionalArgument(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['setting', 'name'], name='setting_optional_argument_primary_key'
            )
        ]

    def __str__(self) -> str:
        return f"{self.setting.test_suite.name}.{self.setting.name}.{self.setting.argument}.{self.name}"

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
    datetime = models.DateTimeField()
    server = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    output_xml = models.CharField(max_length=255)
    log_html = models.CharField(max_length=255)

class RobotExecPositionalArgument(models.Model):
    robot = models.ForeignKey(RobotExec, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    value = models.CharField(max_length=255)

class RobotExecOptionalArgument(models.Model):
    robot = models.ForeignKey(RobotExec, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

