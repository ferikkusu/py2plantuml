
from pathlib import Path
from typing import List


class PythonFileReader:
    lines: List[str]

    def __init__(self, python_file_path: Path) -> None:
        with open(python_file_path, "r") as python_file:
            self.lines = python_file.readlines()

    def find_classes(self) -> List[List[str]]:
        class_lines: List[List[str]] = []
        
        class_definition_indices: List[int] = []
        for line_index in range(len(self.lines)):
            if self.lines[line_index].strip().startswith("class"):
                class_definition_indices.append(line_index)
        
        for i in range(len(class_definition_indices)):
            if i + 1 == len(class_definition_indices):
                class_lines.append(self.lines[class_definition_indices[i]:])
            else:
                class_lines.append(self.lines[class_definition_indices[i]:class_definition_indices[i + 1]])

        return class_lines
    