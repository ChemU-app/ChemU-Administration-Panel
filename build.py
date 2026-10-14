#!/bin/python

import glob
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys

MODULES = ["paramiko"]
INPUTS = ["src/imports.py", "src/GlobalState.py", *sorted(glob.glob("src/gui/*py")), "src/main.py"]

def main():
    print("Checking needed modules")
    try:
        venv_check = importlib.util.find_spec('venv')
        if venv_check is None:
            print("You need the venv python module installed.")
            return
    except ImportError:
        print(ImportError)
        print("You need the venv python module installed.")
        return
    

    print("Creating Virtual Environment")
    try:
        absolute_path = os.path.abspath(__file__)
        directory = os.path.dirname(absolute_path)
        os.chdir(directory)
    except FileNotFoundError:
        print(FileNotFoundError)
        print("Failed to enter script directory")
        return

    try:
        if not os.path.exists("./venv/pyvenv.cfg"):
            process = subprocess.run(["python", "-m", "venv", "./venv"])
        else:
            print("Virtual Environment already exists")
    except:
        print("Failed to create virtual environment")
    try:
        print("moving into virtual environment")
        os.chdir("./venv/")
    except:
        print("FAILED TO MOVE IN")
        return
    try:
        print("Getting pip")
        python_venv = ("./Scripts/python.exe" if sys.platform == "win32" else "./bin/python")
        process = subprocess.run([str(python_venv), "-m", "ensurepip", "--upgrade"], check=True)
    except:
        print("Failed to get pip")
        print("Continuing")
    try:
        print("Installing Python Modules")
        python_venv = ("./Scripts/python.exe" if sys.platform == "win32" else "./bin/python") 
        process = subprocess.run([str(python_venv), "-m", "pip", "install", *MODULES], check=True)
    except:
        print("Failed to install paramiko to virtual environment")
        print("Continuing")
    finally:
        print("Building ChemU Server Admin Tool")
        try:
            os.chdir("../")
            outputFile = Path("./ChemU_Server_Admin_Tool.py")
            with outputFile.open("wb") as output:
                for filename in INPUTS:
                    with open(filename, "rb") as src:
                        shutil.copyfileobj(src, output)
        except:
            print("Failed to build ChemU Server Admin Tool")
            return
        print("Build Complete")
        print("Run run.py")

if __name__ == "__main__":
    main()
