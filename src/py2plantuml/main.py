import argparse
import re

from loguru import logger
from pathlib import Path
from typing import List

from py2plantuml.model import Class
from py2plantuml.parser import ClassParser
from py2plantuml.reader import PythonFileReader


def initialize_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="py2plantuml",
        description="Creates plantuml files from python classes"
    )
    parser.add_argument("-p", "--project_path", type=Path)
    parser.add_argument("-c", "--class_name", type=str)
    parser.add_argument("-o", "--output_path", type=argparse.FileType('w', encoding='utf-8'))
    return parser


def keep_only_specified_class_file(python_file_paths: List[Path], class_name: str) -> Path:
    for path in python_file_paths:
        with open(path, "r") as python_file:
            lines: List[str] = python_file.readlines()
        for line in lines:
            if re.match(f"class {class_name}\((.+)\):", line.strip()) or re.match(f"class {class_name}:", line.strip()):
                return path
    raise ValueError(f"Could not find class '{class_name}'")


if __name__ == "__main__":
    argparser = initialize_argument_parser()
    arguments = argparser.parse_args()

    logger.info(f"Project path: '{arguments.project_path}'")
    logger.info(f"Class name: '{arguments.class_name}'")
    logger.info(f"Output path: '{arguments.output_path}'")

    directory: Path = arguments.project_path
    python_files: List[Path] = list(directory.rglob("*.py"))
    python_file: Path = keep_only_specified_class_file(python_file_paths=python_files, class_name=arguments.class_name)
    
    reader: PythonFileReader = PythonFileReader(python_file_path=python_file)
    classes_line_list: List[List[str]] = reader.find_classes()
    parser: ClassParser = ClassParser()
    
    classes: List[Class] = []
    for class_lines in classes_line_list:
        classes.append(parser.parse(data=class_lines))

    print(classes)
    arguments.output_path.write(classes[0].to_string())