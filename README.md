# test_exercise_for_AQA_Python_2025


A Python 3.11 application that parses an XMI-based UML structure from impulse_test_input.xml and generates two artifacts:

config.xml: Internal hierarchical configuration in XML format
meta.json: Metadata describing classes and their relationships, used by the frontend to display object trees

Requirements

Python 3.11
No third-party libraries required (only standard Python modules)

Usage

1. Place impulse_test_input.xml in the project root.
2. cd ./${project root}
3. Run the program:

python main.py

3. Generated files will appear in the out/ folder.

Output Files

config.xml

Represents the configuration of the base station as a tree structure based on UML class composition.

meta.json

A metadata file describing each UML class, its attributes, relationships, and whether it's a root object. This format is consumed by the frontend.


Design Principles

Object-Oriented Design: Clean separation of model, parsing, and generation logic.
Scalability: Easy to extend for new output formats or input structures.
Maintainability: Modular, testable, and clear file structure.
No External Dependencies: Uses only the Python Standard Library.
