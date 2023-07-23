from pathlib import Path
import json
import tempfile
from typing import Any
from robot.libdoc import libdoc
from django.core.management.base import BaseCommand, CommandParser
from robotlib.models import Library, InitArgument, LibraryKeyword, KeywordArgument, KeywordOptionalArgument


def get(dict, key):
    value = dict[key]

    if value == None:
        return "None"
    
    return value.replace("\\", " ")


def import_library(library_name: str):
    tmp_file = Path(tempfile.gettempdir()) / f"{library_name}.json"
    libdoc(library_name, outfile=str(tmp_file))
    
    with open(tmp_file, encoding='utf-8') as file:
        lib_json = json.load(file)

    lib = Library(
        name=lib_json["name"],
        version=lib_json["version"],
        documentation=lib_json["doc"]
    )
    lib.save()

    for init_arg in lib_json["inits"][0]["args"]:
        if init_arg["name"] in ["_"]:
            continue

        InitArgument(
            library=lib,
            name=init_arg["name"],
            default_value=get(init_arg, "defaultValue")
        ).save()

    for keyword in lib_json["keywords"]:
        kw = LibraryKeyword(
            library=lib,
            name=keyword["name"],
            documentation=keyword["doc"],
            tag=",".join(keyword["tags"])
        )
        kw.save()

        for idx, arg, in enumerate(keyword["args"]):
            if arg["required"]:
                KeywordArgument(
                    keyword=kw,
                    position=idx,
                    name=arg["name"]
                ).save()
            else:
                KeywordOptionalArgument(
                    keyword=kw,
                    name=arg["name"],
                    default_value=get(arg, "defaultValue")
                ).save()


class Command(BaseCommand):
    help = "Imports the specified Robot Framework library"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("library_name", nargs=1, type=str)

    def handle(self, *args: Any, **options: Any) -> None:
        import_library(options["library_name"][0])
