import subprocess
import sys
import os

python_exe = None

# For Linux/Mac:
if os.name == "posix":
    python_exe = os.path.join(sys.prefix, 'bin', 'python3.11')
# For Windows:
else:
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

if python_exe is not None:
    # upgrade pip
    subprocess.call([python_exe, "-m", "ensurepip"])
    subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
     
    # install required packages
    subprocess.call([python_exe, "-m", "pip", "install", "pymeshlab"])

    print("DONE")
else:
    print("Failed to find Python")
