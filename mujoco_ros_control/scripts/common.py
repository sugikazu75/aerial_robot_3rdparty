import os
import subprocess
import sys

def run_subprocess(cmd):
    if sys.version.split(".")[0] == "2":
        subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if sys.version.split(".")[0] == "3":
        subprocess.run(cmd, shell=True)

def get_filename(filepath):
    return os.path.basename(filepath)

def get_directory(filepath):
    return os.path.dirname(filepath)

def get_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return ext

def remove_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return before_ext

def run_xacro(input_path, output_path):
    cmd = "rosrun xacro xacro {} > {}".format(input_path, output_path)
    run_subprocess(cmd)
