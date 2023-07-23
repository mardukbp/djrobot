from typing import Any
import robot
from django.core.management.base import BaseCommand, CommandParser
from testplan.models import TestPlan

def indent(str_list):
    return [
        "    " + str
        for str in str_list
    ]

def append(str, str_list):
    if str:
        return [str] + str_list

    return str_list


def gen_test_suite(library_imports, test_cases):
    return "\n".join(["***Settings***"] + [
        "    ".join(
        ["Library", lib_import["library"]] + [
            f"{name}={value}"
            for name, value in lib_import["args"].items()
        ])
        for lib_import in library_imports
    ] + [""] + ["*** Test Cases ***"] + [
        "\n".join([test_case["name"]] + indent([
            "    ".join(append(kw_call["return_value"], [kw_call["keyword"]] + kw_call["args"] + [
                f"{name}={value}"
                for name, value in kw_call["kwargs"].items()
            ]))
            for kw_call in test_case["test_sequence"]
        ] + [""]))
        for test_case in test_cases
    ])


def gen_library_imports(library_imports):
    return [
        {
            "library": lib_import.library.name,
            "args": {
                arg.name: arg.value
                for arg in lib_import.arguments.all()
            }
        }
        for lib_import in library_imports
    ]


def gen_test_cases(test_cases):
    return [
        {
            "name": test_case.name,
            "test_sequence": [
                {
                    "return_value": keyword_call.return_value,
                    "keyword": keyword_call.keyword_name,
                    "args": [
                        arg.value
                        for arg in keyword_call.args.all().order_by('position')
                    ],
                    "kwargs": {
                        arg.name: arg.value
                        for arg in keyword_call.kwargs.all()
                    }
                }
                for keyword_call in test_case.keyword_calls.all()
            ]
        }
        for test_case in test_cases
    ]


def testplan_to_testsuite(name: str):
    test_plan = TestPlan.objects.get(name=name)
    library_imports = test_plan.library_imports.all()
    test_cases = test_plan.test_cases.all()

    return gen_test_suite(
        gen_library_imports(library_imports),
        gen_test_cases(test_cases)
    )


def execute_testplan(test_plan: str):
    test_suite = testplan_to_testsuite(test_plan)
    print(test_suite)
    # robot.run_cli(test_suite)


class Command(BaseCommand):
    help = "Executes the specified test plan with Robot Framework"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("test_plan_name", nargs=1, type=str)

    def handle(self, *args: Any, **options: Any) -> None:
        execute_testplan(options["test_plan_name"][0])
