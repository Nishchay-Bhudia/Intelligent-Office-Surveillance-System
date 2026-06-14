import subprocess

#process = subprocess.Popen([r"D:\mypython1\python.exe", "miniNEA1.py"])

import sys

# sys.executable automatically replaces the hardcoded path
process = subprocess.Popen([sys.executable, "systemArmed.py"])

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
events_folder = os.path.join(script_dir, "events2")




process.terminate()

#if system armed --. run l3, else, run l5
