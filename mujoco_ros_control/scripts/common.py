import os
import subprocess
import sys

def run_subprocess(cmd):
    if sys.version.split(".")[0] == "2":
        subprocess.call(cmd, shell=True)
    if sys.version.split(".")[0] == "3":
        subprocess.run(cmd, shell=True)


def get_filename(filepath):
    return filepath.rsplit("/", 1)[1]


def get_directory(filepath):
    return filepath.rsplit("/", 1)[0]


def get_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return ext

def remove_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return before_ext


def run_xacro(input_path, output_path):
    cmd = "rosrun xacro xacro {} > {}".format(input_path, output_path)
    run_subprocess(cmd)
