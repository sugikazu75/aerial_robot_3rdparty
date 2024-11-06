#!/usr/bin/env python
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

def get_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return ext

def remove_extension(filename):
    before_ext, ext = os.path.splitext(filename)
    return before_ext

def dae2stl(dae_path, stl_path):
    cmd = "meshlabserver -i {} -o {}".format(dae_path, stl_path)
    run_subprocess(cmd)

def main():
    if len(sys.argv) == 2:
        dae_path = sys.argv[1]
        stl_path = remove_extension(dae_path) + ".stl"
        if(get_extension(dae_path) == ".dae"):
            print("convert", dae_path, "to", stl_path)
            dae2stl(dae_path, stl_path)
        else:
            print("extension of", dae_path, "is not .dae")
            return
    else:
        print("variable error")

if __name__ == "__main__":
    main()
