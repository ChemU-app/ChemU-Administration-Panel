#!/bin/python

from pathlib import Path
import subprocess
import sys

base_dir = Path(__file__).resolve().parent
venv_dir = base_dir / "venv"

if sys.platform == "win32":
    python = venv_dir / "Scripts" / "python.exe"
else:
    python = venv_dir / "bin" / "python"

script = base_dir / "ChemU_Server_Admin_Tool.py"

if not python.exists():
    raise FileNotFoundError(f"Virtual-environment Python not found: {python}")

if not script.exists():
    raise FileNotFoundError(f"Application script not found: {script}")

result = subprocess.run([str(python), str(script)], cwd=base_dir)
raise SystemExit(result.returncode)

