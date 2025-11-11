#This software is provided for "educational and experimental purposes only".
#It is "NOT intended for production use".  
#By using this code, you agree that you assume "ALL risks" and the author is "NOT liable" for any damages, losses, or consequences.

import importlib
import pathlib

def test_imports():
    project_root = pathlib.Path(__file__).parent
    python_files = project_root.glob("*.py")

    for file in python_files:
        module_name = file.stem
        try:
            importlib.import_module(module_name)
        except Exception as e:

            raise AssertionError(f"Failed to import {module_name}: {e}")
