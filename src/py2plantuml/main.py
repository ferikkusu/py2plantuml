import argparse

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


if __name__ == "__main__":
    argparser = initialize_argument_parser()
    arguments = argparser.parse_args()

    logger.info(f"Project path: '{arguments.project_path}'")
    logger.info(f"Class name: '{arguments.class_name}'")
    logger.info(f"Output path: '{arguments.output_path}'")

    directory: Path = arguments.project_path
    python_files: List[Path] = list(directory.rglob("*.py"))
    reader: PythonFileReader
    for python_file in python_files:
        tmp_reader: PythonFileReader = PythonFileReader(python_file_path=python_file)
        if tmp_reader.contains_specified_class_definition(class_name=arguments.class_name):
            reader = tmp_reader
            break

    classes_line_list: List[List[str]] = reader.find_classes()
    parser: ClassParser = ClassParser()
    
    classes: List[Class] = []
    for class_lines in classes_line_list:
        classes.append(parser.parse(data=class_lines))

    print(classes)
    arguments.output_path.write(classes[0].to_string())