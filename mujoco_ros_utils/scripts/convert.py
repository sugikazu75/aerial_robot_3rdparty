import os.path
import sys
import glob
import subprocess


def config_dir():
    """This package's config/ directory.

    It sits beside the scripts in the source tree and in share/, but not in
    lib/<pkg>/ - which is where `ros2 run` starts them from. So look next door
    first and fall back to the ament index.
    """
    beside = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config"))
    if os.path.isdir(beside):
        return beside

    from ament_index_python.packages import get_package_share_directory
    return os.path.join(get_package_share_directory("mujoco_ros_utils"), "config")

def run_subprocess(cmd):
    if sys.version.split(".")[0] == "2":
        subprocess.call(cmd, shell=True)
    if sys.version.split(".")[0] == "3":
        subprocess.run(cmd, shell=True)

def convert_dae_to_stl(input_file, output_file):
    filter_path = os.path.join(config_dir(), "filter.mxl")

    cmd = "xvfb-run -a meshlabserver -i {} -o {} -m binary -s {}".format(input_file, output_file, filter_path)
    run_subprocess(cmd)
