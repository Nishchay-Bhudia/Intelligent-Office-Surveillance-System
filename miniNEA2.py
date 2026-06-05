import shutil
import os

# Get the directory where THIS script file is stored
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join that directory with your folder names
saved_path = os.path.join(script_dir, "saved")
temp_path = os.path.join(script_dir, "temporary")

if os.path.exists(saved_path):
    shutil.rmtree(saved_path)
    os.makedirs(saved_path)

if os.path.exists(temp_path):
    shutil.rmtree(temp_path)
    os.makedirs(temp_path)
