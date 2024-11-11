# $ blender -b -P convert.py -- meshdir

import bpy
import os.path
import sys
import glob

def delete_all():
    if bpy.app.version[1] > 80:
        for item in bpy.data.meshes:
            bpy.data.meshes.remove(item, do_unlink=True)

    if bpy.app.version[1] <= 79:
        for item in bpy.data.meshes:
            bpy.data.meshes.remove(item)

def dae2stl(input_dae_path, output_stl_path):
    delete_all()
    bpy.ops.wm.collada_import(filepath=input_dae_path)
    bpy.ops.export_mesh.stl(filepath=output_stl_path)

def main():
    if len(sys.argv) == 7:
        dae_path = sys.argv[5]
        stl_path = sys.argv[6]
        delete_all()
        dae2stl(dae_path, stl_path)
    else:
        print("variable error")

if __name__ == "__main__":
    main()
