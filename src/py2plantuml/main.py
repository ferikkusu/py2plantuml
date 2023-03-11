import argparse

from loguru import logger
from pathlib import Path


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
    parser = initialize_argument_parser()
    arguments = parser.parse_args()

    logger.info(f"Project path: '{arguments.project_path}'")
    logger.info(f"Class name: '{arguments.class_name}'")
    logger.info(f"Output path: '{arguments.output_path}'")
