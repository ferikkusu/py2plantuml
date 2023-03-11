#!/bin/bash
mypy src/py2plantuml
pytest --cov --cov-report xml:coverage.xml