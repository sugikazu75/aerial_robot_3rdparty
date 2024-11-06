#!/usr/bin/env python

from common import *
import sys

def dae2stl(dae_path, stl_path):
    cmd = "meshlabserver -i {} -o {} > /dev/null 2>&1".format(dae_path, stl_path)
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
